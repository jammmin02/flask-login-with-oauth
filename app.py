# Flask 웹 프레임워크 및 세션, 리다이렉션 등 관련 모듈 임포트
from flask import Flask, session, abort, redirect, request
from google_auth_oauthlib.flow import Flow      # OAuth 2.0 흐름 관리 모듈 임포트
import os                                       # 운영체제 관련 모듈 임포트
import pathlib                                  # 파일 경로 조작 모듈 임포트
import google.auth.transport.requests           # Google 인증 요청 모듈 임포트
import google.oauth2.id_token                   # Google ID 토큰 검증 모듈 임포트    

# 로컬 HTTP 콜백 허용  (개발용) -> https 없이 테스트 가능
# - 기본적으로 OAuth는 https(보안 연결)만 허용하지만
#   로컬 테스트를 위해 http도 허용하도록 강제로 설정
# - 실제 서비스(운영 환경)에서는 절대 사용하면 안 됨
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask("google login app")                # Flask 앱 생성
app.secret_key = "CodeSpecialist.com"          # 세션 암호화 키 설정

# 클라이언트 ID 및 클라이언트 시크릿 파일 경로 설정
GOOGLE_CLIENT_ID = (
    "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com" # 여기에 실제 클라이언트 ID 입력
)

# 클라이언트 시크릿 파일 경로 설정 (현재 파일 기준 상대 경로)
client_secret_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

# OAuth 2.0 클라이언트 구성
# - 인증 URL 생성, 콜백에서 코드 → 토큰 교환까지의 흐름을 담당하는 객체
flow = Flow.from_client_secrets_file(
    # 클라이언트 시크릿 파일 경로
    client_secret_file,
    # scope 설정
    # - 사용자 프로필 및 이메일 정보 접근 권한 요청
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile", # 사용자 프로필 정보 접근 권한
        "https://www.googleapis.com/auth/userinfo.email",   # 사용자 이메일 정보 접근 권한
        "openid",                                           # ID 토큰(사용자 식별 정보) 요청
    ],
    # 리디렉션 URI 설정
    redirect_uri="http://127.0.0.1:5000/callback",
)

# 인증 보호 데코레이터
# - 데코레이터란 특정 함수(또는 메서드) 앞에 붙어서 그 함수의 동작을 감싸는 함수
# - 로그인된 사용자만 접근 허용
def login_is_required(function):
    # wrapper 함수 정의 : 실제 함수 호출 전 로그인 상태 확인
    def wrapper(*args, **kwargs): 
        # 세션에 google_id가 없으면 (로그인 안된 상태) -> 401 오류 반환      
        if "google_id" not in session:  
            return abort(401)  
        
        # 로그인된 경우, 원래 함수 호출
        return function(*args, **kwargs)
    
    return wrapper

# 로그인 라우트
# - Google OAuth 2.0 인증 시작
# - 사용자에게 Google 로그인 페이지로 리디렉션
@app.route("/login")
def login():
    # 구글 인증 서버로 리디렉션할 URL 생성
    # prompt="select_account" 옵션 추가: 계정 선택 화면 강제 표시
    authorization_url, state = flow.authorization_url(prompt="select_account")
    session["state"] = state                # CSRF 방지를 위한 상태 토큰 저장
    return redirect(authorization_url)      # 구글 인증 서버로 리디렉션

#  callback 라우트
# - 구글 인증 후 리디렉션되는 URI
# - 토큰 요청 및 사용자 정보 검증
@app.route("/callback")
def callback():
    # 구글 토큰 서버에 토큰 요청
    flow.fetch_token(authorization_response=request.url)

    # CSRF 방지: 로그인 시작 시 저장한 state와 콜백으로 돌아온 state가 같은지 확인
    # - 둘이 다르면, 내가 보낸 요청에서 온 콜백이 아니므로 공격 가능성이 있다고 판단
    if not session["state"] == request.args.get("state"):
        abort(400) # 잘못된 요청

    # 인증된 사용자 자격 증명 획득
    credentials = flow.credentials
    
    # Google 인증 요청 객체 생성
    req = google.auth.transport.requests.Request()

    # ID 토큰 검증
    # - 토큰이 실제 Google이 발급한 것인지
    # - 이 클라이언트(GOOGLE_CLIENT_ID)를 대상으로 발급된 것인지(audience 검증)
    # - 만료되지는 않았는지 등을 확인
    # - clock_skew_in_seconds: 서버/클라이언트 간 시간 차이를 몇 초까지 허용할지
    id_info = google.oauth2.id_token.verify_oauth2_token(
              id_token=credentials.id_token,  # ID 토큰
              request=req,                    # 요청 객체
              audience=GOOGLE_CLIENT_ID,      # 클라이언트 ID
              clock_skew_in_seconds=300,      # 시간 오차 허용 범위 (초)
            )
    
    # 세션에 사용자 정보 저장
    session["google_id"] = id_info.get("sub") # 고유 사용자 ID
    session["name"] = id_info.get("name")     # 사용자 이름
    return redirect("/protected_area")        # 보호된 영역(protected_area)으로 리디렉션

# 로그아웃 라우트
# - 세션 정보 삭제 후 메인 페이지로 리디렉션
@app.route("/logout")
def logout():
    session.clear()       # 세션 정보 삭제
    return redirect("/")  # 메인 페이지로 리디렉션

# 메인 페이지 라우트
# - 간단한 인덱스 페이지 제공
# - 로그인 버튼 표시
@app.route("/")
def index():
    return "Google Login <br><a href='/login'><button>login</button></a>"

# 보호된 영역 라우트
# - 로그인된 사용자만 접근 가능
# - 사용자 이름과 로그아웃 버튼 표시
@app.route("/protected_area")
@login_is_required  # 인증 보호 함수 호출 
def protected_area():
    return f"Hello {session['name']}! <br><a href='/logout'><button>logout</button></a>"

# 애플리케이션 실행
# - main 모듈로 실행될 때만 실행
# - debug = True -> 오류 발생 시 상세 정보 제공 
# - 개발 중에만 사용, 배포 시에는 False로 설정
if __name__ == "__main__":
    app.run(debug=True) # 애플리케이션 실행
