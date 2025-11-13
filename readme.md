# Flask Login with OAuth

간단한 Flask 기반의 OAuth 2.0 / OpenID Connect 로그인 흐름을 학습하기 위한 최소 예제입니다.

---

## 요약

- **목적:** OAuth/OpenID Connect 로그인 흐름 학습용 경량 예제
- **언어:** Python
- **프레임워크:** Flask

## Prerequisites (사전 준비)

- Python 3.8 이상
- Git

## 프로젝트 구조 (주요 파일)

- `app.py` — 샘플 Flask 애플리케이션
- `client_secret.json` — OAuth 클라이언트 비밀 파일 (로컬에서 관리)
- `requirements.txt` — 필요한 패키지 목록

---

## 빠른 시작

1) 저장소 클론

```bash
git clone https://github.com/USERNAME/flask-login-with-oauth.git
cd flask-login-with-oauth
```

2) 가상환경 생성

Windows (PowerShell):

```powershell
python -m venv venv
```

macOS / Linux:

```bash
python3 -m venv venv
```

3) 가상환경 활성화

Windows (PowerShell):

```powershell
venv\Scripts\Activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

4) 의존성 설치

```bash
pip install -r requirements.txt
```

5) 설정 파일 준비

- Google Cloud Console에서 발급받은 `client_secret.json`을 프로젝트 루트에 두세요.

---

## Google Cloud Console에서 클라이언트 ID 발급 받기

간단한 단계로 정리했습니다. 개발 중에는 `External` 사용자 유형을 사용하고, 테스트 사용자에 본인 계정을 추가하세요.

1. Google Cloud Console 접속

- `https://console.cloud.google.com/`에 접속해 로그인합니다.

2. 프로젝트 선택/생성

- 좌측 상단의 프로젝트 드롭다운에서 새 프로젝트를 만들거나 기존 프로젝트를 선택합니다.

3. OAuth 동의 화면 구성

- `APIs & Services` -> `OAuth consent screen`으로 이동합니다.
- 사용자 유형(Internal/External)을 선택하고 앱 이름, 지원 이메일 등을 입력합니다.
- External인 경우 테스트 사용자(Test users)에 본인 이메일을 추가하세요.

4. OAuth 클라이언트 ID 생성

- `APIs & Services` -> `Credentials`로 이동합니다.
- `Create Credentials` -> `OAuth client ID` 선택
- Application type은 `Web application` 선택, `Name`은 구분하기 쉬운 이름으로 입력

5. 승인된 리디렉션 URI 추가

- 로컬 개발 기본값: `http://127.0.0.1:5000/callback`
- 필요하면 `http://localhost:5000/callback`도 추가하세요.
- (중요) `app.py`의 `redirect_uri` 값과 정확히 일치시켜야 합니다.

6. 클라이언트 ID 발급 및 JSON 다운로드

- 생성 후 `Download`를 눌러 `client_secret.json`을 내려받아 프로젝트 루트에 두세요.
- 절대 공개 저장소에 업로드하지 마세요.

7. 테스트

- 앱을 실행한 뒤 `/` 경로로 접속해 로그인 흐름을 확인하세요.

---

## 애플리케이션 실행

```powershell
flask run --debug
```

또는

```powershell
python app.py
```

## 유의사항

- `client_secret.json` 같은 민감 정보는 절대 공개 저장소에 커밋하지 마세요.
- 로컬 개발 중에는 `OAUTHLIB_INSECURE_TRANSPORT=1`을 사용하지만, 운영 환경에서는 HTTPS를 반드시 사용하세요.
- `app.py`의 `GOOGLE_CLIENT_ID`와 `redirect_uri`가 Google Cloud Console 설정과 일치하는지 확인하세요.

---
