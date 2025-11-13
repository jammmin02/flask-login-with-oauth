---flask login with oauth

간단한 Flask 기반 OAuth 2.0 & OpenID Connect 로그인 흐름을 실습하기 위한 최소 예제 프로젝트입니다.

**요약**
- **목적:** OAuth/OpenID Connect 로그인 흐름 학습용 경량 예제
- **언어:** Python
- **프레임워크:** Flask

**Prerequisites (사전 준비)**
- Python 3.8 이상
- Git

**프로젝트 구조 (주요 파일)**
- `app.py`: 샘플 Flask 애플리케이션
- `client_secret.json`: OAuth 클라이언트 비밀 파일 (로컬에서 관리)
- `requirements.txt`: 필요한 패키지 목록

**설치 및 실행 (빠른 시작)**

1. 저장소 클론

```
git clone https://github.com/USERNAME/flask-login-with-oauth.git
```

2. 가상환경 생성

- Windows (PowerShell)

```
python -m venv venv
```

- macOS / Linux

```
python3 -m venv venv
```

3. 가상환경 활성화

- Windows (PowerShell)

```
venv\Scripts\Activate
```

- macOS / Linux

```
source venv/bin/activate
```

4. 의존성 설치

```
pip install -r requirements.txt
```

5. 설정 파일 준비
- OAuth 클라이언트 설정(`client_secret.json`)을 프로젝트 루트에 위치시키세요. (공개 저장소에 업로드하지 마세요)

**Google Cloud Console에서 클라이언트 ID 발급 받기**

1. Google Cloud Console 접속

- 브라우저에서 `https://console.cloud.google.com/`에 접속하고 Google 계정으로 로그인합니다.

2. API 및 서비스 선택

- 아래쪽 API 및 서비스 선택에 들어갑니다

3. OAuth 동의 화면 구성
- `APIs & Services` → `OAuth consent screen`으로 이동합니다.
- client(클라이언트)로 이동합니다
- 상단의 클라이언트 만들기를 눌러 이동합니다

4. OAuth 클라이언트 ID 생성
- `APIs & Services` → `Credentials`으로 이동합니다.
- `Create Credentials` → `OAuth client ID`를 선택합니다.
- Application type은 `Web application`을 선택합니다.
- `Name`은 자유롭게 입력합니다.

5. 승인된 리디렉션 URI 추가

- 로컬 개발 환경에서 이 예제의 기본 리디렉션 URI는 `http://127.0.0.1:5000/callback` 입니다.
- 필요하다면 `http://localhost:5000/callback`도 추가하세요.
- (참고: `app.py`의 `redirect_uri` 값을 확인해 동일하게 설정해야 합니다.)

6. 클라이언트 ID 발급 및 JSON 다운로드

- 생성이 완료되면 `Download` 버튼을 눌러 `client_secret.json` 파일을 내려받습니다.
- 이 파일을 프로젝트 루트(``client_secret.json``)에 넣으세요. 절대 공개 저장소에 올리지 마세요.

7. 테스트

- 애플리케이션을 실행하고(``python app.py`` 또는 ``flask run``) `/login` 경로로 접속해 Google 로그인이 동작하는지 확인합니다.


6. 애플리케이션 실행

```
flask run --debug
```

또는

```
python app.py
```

**유의사항**
- `client_secret.json`과 같은 민감 정보는 절대 공개 저장소에 커밋하지 마세요.
- 로컬에서 OAuth 공급자 설정(리디렉션 URI 등)을 정확히 맞춰야 정상 동작합니다.
