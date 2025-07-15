from typing import List, Dict

async def analyze_pose_data(keypoints: List[Dict]) -> str:
    """
    포즈 데이터를 분석하고 Gemini API에 전달할 프롬프트를 생성합니다.
    초기 버전에서는 간단한 분석을 수행합니다.
    """
    # 예시: 특정 관절의 존재 여부 확인
    # 실제 구현에서는 관절 각도, 움직임 패턴 등을 분석합니다.
    if not keypoints:
        return "운동 자세 데이터가 없습니다. 자세를 인식할 수 없습니다."

    # 간단한 관절 위치 기반 피드백 (예시)
    feedback_messages = []
    for kp in keypoints:
        if kp.get("name") == "left_shoulder" and kp.get("y", 0) < 0.3:
            feedback_messages.append("왼쪽 어깨가 너무 낮습니다. 좀 더 들어 올리세요.")
        if kp.get("name") == "right_knee" and kp.get("x", 0) > 0.7:
            feedback_messages.append("오른쪽 무릎이 너무 바깥으로 나갔습니다. 안쪽으로 모으세요.")

    if feedback_messages:
        return "\n".join(feedback_messages)
    else:
        return "현재 자세는 양호합니다. 계속 유지하세요!"

