# 🚀 BoostCoach (채찍피티) 개발 온보딩 지시서

---

## 📘 1. 프로젝트 개요

**프로젝트명**: BoostCoach (채찍피티)  
**목적**: 온디바이스 비전과 AI를 결합한 개인 맞춤형 운동 코칭 앱  
**주요 기능**  
1. 모바일 카메라 비전 기반 운동 인식 (관절·얼굴 추적)  
2. 속도·품질 분석 → 자극적 코칭 메시지 (Gemini API)  
3. SNS 공유용 9:16 리포트 자동 생성 및 공유 버튼  
4. 업로드 영상 분석 리포트 (Twelve Labs API)  
5. 하루 VLOG 자동 편집 (5초 클립 추출)  

---

## 🛠️ 2. 개발 환경 및 툴

```bash
# 공통 설치
Node.js ≥ v18
Yarn 또는 npm
Git CLI
Docker (PostgreSQL 개발)

# 프론트엔드
npm install -g expo-cli

# (옵션) Railway CLI
npm install -g railway
구분	기술/툴
프론트엔드	React Native (Expo)
백엔드	Python + FastAPI
DB & ORM	PostgreSQL + Prisma
인증	Firebase Auth / JWT
AI 연동	OpenAI GPT-4, Gemini API, Twelve Labs API
비전 모델	MediaPipe / BlazePose / MoveNet, ONNX/TFLite
배포	Railway (백엔드), Expo EAS (앱 빌드)
모니터링	Sentry

📂 3. 레포지토리 구조
plaintext
복사
편집
boostcoach/
├── backend/
│   ├── controllers/        # 비즈니스 로직
│   ├── routes/             # Express/FastAPI 라우트
│   ├── services/           # 외부 API 호출 (OpenAI, Gemini, Twelve Labs)
│   ├── middleware/         # 인증, 로깅 등
│   ├── prisma/             # Prisma 스키마 & 마이그레이션
│   ├── Dockerfile
│   ├── .env.example
│   └── package.json
├── frontend/
│   ├── components/         # 공통 컴포넌트
│   ├── screens/            # 화면 단위
│   ├── assets/             # 이미지, 폰트 등
│   ├── App.tsx
│   ├── Dockerfile
│   └── package.json
├── .github/
│   └── workflows/
│       └── ci-deploy.yml   # CI/CD 설정 예시
├── docs/
│   ├── API_SPEC.md
│   ├── DESIGN_GUIDELINES.md
│   ├── ERD.png
│   └── AI_PROMPTS.md
├── .devcontainer/          # VS Code Remote-Container 설정
│   └── devcontainer.json
├── docker-compose.yml
├── README.md
└── LICENSE
⚙️ 4. 로컬 개발 환경 설정
4.1 백엔드
bash
복사
편집
cd backend
cp .env.example .env
# .env 작성:
# OPENAI_API_KEY=
# GEMINI_API_KEY=
# TWELVE_LABS_API_KEY=
# DATABASE_URL=
# FIREBASE_API_KEY=

npm install
npx prisma generate
npx prisma migrate dev --name init
npm run dev   # http://localhost:3000
4.2 프론트엔드
bash
복사
편집
cd frontend
yarn install
expo start    # Expo Go 또는 에뮬레이터
🚀 5. GitHub + Railway CI/CD
5.1 브랜치 전략
main → Production

develop → Staging/QA

feature/*, fix/*, chore/* → 작업용

5.2 Railway 연동
Railway → New Project → “Deploy from GitHub repo”

Repo: boostcoach/backend

Branch: main

Root Directory: backend/

Plugins → PostgreSQL 추가 → 자동 발급된 DATABASE_URL 복사

Settings → Variables 등록

text
복사
편집
OPENAI_API_KEY=
GEMINI_API_KEY=
TWELVE_LABS_API_KEY=
DATABASE_URL=
FIREBASE_API_KEY=
SENTRY_DSN=
5.3 자동 배포 흐름
plaintext
복사
편집
GitHub Push (main)
   ↓
Railway Webhook
   ↓
Docker 이미지 빌드
   ↓
Production 배포
🏛 6. 시스템 아키텍처
클라이언트 (Expo RN)

API Gateway (Express/FastAPI)

서비스 계층

Vision Service → 관절·얼굴 모델

Analysis Service → LLM/Gemini

Report Service → Canvas API

VLOG Service → FFmpeg 기반 편집

데이터 저장소: PostgreSQL

외부 API: OpenAI, Gemini, Twelve Labs

캐시 (옵션): Redis

(별도 docs/architecture.drawio 다이어그램 참조)

🌐 7. 환경 분리 전략
환경	GitHub 브랜치	Railway Project	DB 인스턴스	Sentry DSN
Development	develop	BoostCoach-Dev	postgres-dev	dsn-dev
Staging	staging	BoostCoach-Staging	postgres-stg	dsn-stg
Production	main	BoostCoach-Prod	postgres-prod	dsn-prod

🐳 8. 컨테이너 & 개발자용 Devcontainer
docker-compose.yml
yaml
복사
편집
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - '3000:3000'
    env_file:
      - backend/.env
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - '19000:19000'
    env_file:
      - frontend/.env

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: boostcoach
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
.devcontainer/devcontainer.json
json
복사
편집
{
  "name": "BoostCoach",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "backend",
  "workspaceFolder": "/workspace",
  "extensions": ["ms-azuretools.vscode-docker","esbenp.prettier-vscode"],
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  }
}
🔖 9. API 버전 관리 & 문서화
경로: /api/v1/..., /api/v2/...

Swagger/OpenAPI 자동 생성 (Swagger UI at /docs)

Postman Collection: docs/BoostCoach.postman_collection.json

📝 10. 예외 처리 & 로깅
표준 응답 포맷

json
복사
편집
{ "success": true, "data": {...}, "error": null }
로깅: Winston (backend/services/logger.js)

에러 핸들러: Sentry 통합 (middleware/errorHandler.js)

📊 11. 모니터링 & 메트릭
헬스 체크: GET /healthz

Prometheus → Grafana 대시보드

요청률, 응답 시간, 에러율

Sentry: 예외 및 크래시 추적

🔐 12. 보안 & 인증
인증: Firebase Auth → 발급 토큰 검증 미들웨어

JWT: Access/Refresh 토큰

OAuth2: SNS 로그인 준비(추후 구현)

환경변수 관리: Railway Secrets, GitHub Secrets

✅ 13. 테스트 & 품질 보증
유닛 테스트: Jest (backend/frontend)

E2E 테스트: Detox (RN), Postman/Newman (API)

커버리지: Codecov 연동 → README 뱃지

린트: ESLint + Prettier (npm run lint)

🏷 14. 릴리즈 & 버전 관리
SemVer: MAJOR.MINOR.PATCH

GitHub Releases 템플릿 (릴리즈 노트 자동화)

CHANGELOG.md 유지

💾 15. 백업 & 롤백 플랜
DB 백업: Railway 자동 스냅샷(일일)

롤백:

Railway CLI: railway up --rollback <deployment-id>

Docker 이미지 태그 → 이전 태그로 재배포