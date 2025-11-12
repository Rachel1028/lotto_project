# 🎲 Lotto Project (Django + Docker)

**개발 환경:** macOS · VSCode · Python 3.12 · Django 5.1.2 · Docker

---

## 🧩 프로젝트 개요
이 프로젝트는 **Django 웹 프레임워크와 Docker**를 활용하여  
로또 번호 구매 및 조회가 가능한 간단한 웹사이트를 구축했습니다.

- 사용자는 수동 또는 자동으로 로또 번호를 구매할 수 있습니다.  
- 구매된 번호는 SQLite 데이터베이스에 저장됩니다.  
- Docker를 이용하여 개발 환경을 컨테이너로 통합하였습니다.

---

## 🧱 기술 스택
| 구분 | 사용 기술 |
|------|------------|
| Backend | Django 5.1.2 (Python) |
| Database | SQLite3 |
| Container | Docker, Docker Compose |
| IDE | Visual Studio Code |
| OS | macOS |

---

## ⚙️ 주요 기능
| 기능 | 설명 |
|------|------|
| 🎰 **로또 구매** | 사용자가 번호를 직접 입력(수동) 또는 자동 생성 가능 |
| 📋 **구매 내역 확인** | 구매한 번호를 목록 형태로 확인 |
| 🧮 **자동 번호 생성** | `random.sample()`을 사용하여 1~45 사이 6개 번호 자동 생성 |
| 🐳 **Docker 배포** | Django 서버를 Docker 컨테이너로 실행 가능 |

---

## 🗂 프로젝트 구조
lotto_project/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── lotto_site/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── lotto/
├── models.py
├── views.py
├── urls.py
└── templates/
├── home.html
└── buy.html

→ 브라우저에서 접속
http://127.0.0.1:8000/

🐳 2. Docker 환경에서 실행
→ 브라우저에서 접속
http://localhost:8000/

🧰 Docker 명령어 요약
명령	설명
docker compose up --build	컨테이너 빌드 및 실행
docker compose down	컨테이너 종료
docker ps	실행 중인 컨테이너 목록 확인
docker logs [컨테이너ID]	로그 확인

📚 참고 문헌
* Django 공식문서
* Docker 공식문서
* Python random 모듈 공식 문서

✨ 작성자
* Name: Heo Yunseo
* GitHub: @Rachel1028
* Project Repository: https://github.com/Rachel1028/lotto_project
