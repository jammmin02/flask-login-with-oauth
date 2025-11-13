flask login with oauth

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