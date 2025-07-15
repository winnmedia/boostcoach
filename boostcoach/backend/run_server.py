import os
from dotenv import load_dotenv
import uvicorn

# .env 파일 로드
load_dotenv()

# 환경 변수 확인 (선택 사항, 디버깅용)
print(f"GEMINI_API_KEY: {os.getenv('GEMINI_API_KEY')}")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True, log_level="debug")
