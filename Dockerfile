# 베이스 이미지 (Python 3.12 버전 사용)
FROM python:3.12-slim

# 컨테이너 안의 작업 디렉토리 지정
WORKDIR /app

# 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 전체 복사
COPY . .

# 포트 개방 (Django의 기본 포트)
EXPOSE 8000

# 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
