from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from services.gemini_service import get_gemini_response
from services.exercise_analysis_service import analyze_pose_data

router = APIRouter()

class PoseData(BaseModel):
    keypoints: List[Dict] # Example: [{"x": 0.5, "y": 0.5, "score": 0.9}, ...]
    # Add other relevant pose data fields as needed, e.g., frame_timestamp, user_id

@router.post("/analyze_exercise")
async def analyze_exercise(pose_data: PoseData):
    try:
        # 1. 포즈 데이터 분석
        analysis_result = await analyze_pose_data(pose_data.keypoints)

        # 2. Gemini API에 전달할 프롬프트 생성
        # 실제 프롬프트는 analysis_result를 기반으로 더 정교하게 생성됩니다.
        prompt = f"사용자의 운동 자세 데이터 분석 결과: {analysis_result}. 이 분석을 바탕으로 사용자에게 자극적이고 동기 부여가 되는 코칭 메시지를 200자 이내로 제공해주세요."
        
        # 3. Gemini API 호출
        feedback = await get_gemini_response(prompt)
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
