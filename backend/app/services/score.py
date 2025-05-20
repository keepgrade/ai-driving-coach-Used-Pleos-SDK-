def calculate_score(speed: float, brake_count: int) -> int:
    # 예시 로직: 속도와 급제동 수를 반영한 점수
    base = 100
    penalty = int(brake_count * 5)
    return max(0, base - penalty)
