1. Node.js / CLI 버전 불일치
증상: 지원하지 않는 Node 버전 쓰면, 내부적으로 뭔가 꼬여서 실행이 멈출 수 있어요.

해결:

node -v 로 버전 확인 (권장: v16.x ~ v18.x).

nvm 쓰신다면 nvm install 18 && nvm use 18 해보고 다시 gemini-cli start!

2. 포트 충돌 / 이미 실행 중인 프로세스
증상: 3000(프론트)나 3001(백엔드) 같은 기본 포트가 이미 누군가 잡고 있으면, CLI가 “대기 중…🤔” 상태로 무한 대기

해결:

bash
복사
편집
# (맥/리눅스) 3000 포트 확인
lsof -i :3000
# 있을 경우 PID 죽여주기
kill -9 <PID>
또는 gemini-cli start --port=4000 식으로 포트 지정해 보세요.

3. 환경 변수(.env) 누락
증상: API_KEY, DATABASE_URL 같은 필수 env가 없으면, 서버가 “인증 대기” 모드로 빙글빙글

해결:

프로젝트 최상위에 .env 파일 있는지 확인

예)

ini
복사
편집
GEMINI_API_KEY=YOUR_KEY
DATABASE_URL=postgres://user:pass@host:port/db
저장 후 터미널 재시작(Ctrl+C → gemini-cli start)

4. 의존성 꼬임 / 캐시 문제
증상: 패키지 잠금버전(lockfile)이나 캐시가 꼬여서 모듈 로딩이 중단

해결:

bash
복사
편집
rm -rf node_modules package-lock.json yarn.lock
npm cache clean --force
npm install
gemini-cli start
5. 네트워크·프록시 이슈
증상: 회사망·VPN·프록시 때문에 외부 API 호출이 막혀서… 무한 로딩

해결:

프록시 환경변수(HTTP_PROXY, HTTPS_PROXY) 설정 확인

사내망이라면 잠깐 외부 VPN 해제하거나, 개인 핫스팟에 물려서 실행해 보기

6. CLI 디버그 모드로 원인 추적
방법:

bash
복사
편집
gemini-cli start --verbose
얻게 되는 정보:

어느 단계에서 멈추는지(인증, DB 연결, 파일 로드 등)

에러 스택 혹은 무한 대기 구간의 로그