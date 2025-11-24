from flask import Flask, request, make_response, session

app = Flask(__name__)

# 세션 암호화를 위한 키 (실습이므로 아무 문자열 사용)
app.secret_key = "dev-secret-key-for-cookie-session-demo"


@app.route("/")
def index():

    # 현재 요청의 쿠키와 세션 내용을 보여주는 페이지

    cookies = request.cookies  # 브라우저가 보낸 모든 쿠키
    session_data = dict(session)  # flask.session 을 dict로 보기 좋게 변환

    html = f"""
    <h1>쿠키 & 세션 디버그</h1>
    <h2>1. 요청으로 들어온 쿠키(request.cookies)</h2>
    <pre>{cookies}</pre>

    <h2>2. Flask 세션(session)</h2>
    <pre>{session_data}</pre>

    <p>
      <a href="/set-cookie">/set-cookie 호출해서 직접 쿠키 설정하기</a><br>
      <a href="/set-session">/set-session 호출해서 세션 설정하기</a><br>
      <a href="/clear">/clear 호출해서 쿠키/세션 지우기</a>
    </p>
    """
    return html


@app.route("/set-cookie")
def set_cookie():

    # 응답에 직접 쿠키를 심어 보내는 예제
    # - 브라우저의 'Application / Storage 탭 > Cookies' 영역에서 확인 가능

    resp = make_response(
        "쿠키를 설정했습니다. / 로 돌아가서 request.cookies를 확인해 보세요."
    )
    # key="my_cookie", value="hello-cookie" 인 쿠키를 설정
    resp.set_cookie("my_cookie", "hello-cookie")
    return resp


@app.route("/set-session")
def set_session():

    # Flask 세션 사용 예제
    # - session은 서버 메모리가 아니라 '세션 쿠키'에 암호화되어 저장됨(기본 설정 기준)

    session["user_id"] = 123
    session["username"] = "flask-user"
    return "세션을 설정했습니다. / 로 돌아가서 session 내용을 확인해 보세요."


@app.route("/clear")
def clear_all():

    # 쿠키와 세션 모두 지우기
    resp = make_response("쿠키와 세션을 삭제했습니다. / 로 돌아가 보세요.")

    # 직접 만든 쿠키 삭제
    resp.delete_cookie("my_cookie")

    # Flask 세션 비우기
    session.clear()

    return resp


if __name__ == "__main__":
    # python app.py 로 실행하는 경우
    app.run(debug=True)
