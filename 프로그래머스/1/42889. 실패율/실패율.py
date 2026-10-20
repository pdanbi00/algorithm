def solution(N, stages):
    result = []
    total_players = len(stages)
    
    for i in range(1, N + 1):
        if total_players == 0:
            fail_rate = 0
        else:
            count = stages.count(i)
            fail_rate = count / total_players
            total_players -= count
        result.append((i, fail_rate))
    
    # 실패율 기준 내림차순, 실패율 같으면 스테이지 번호 기준 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, _ in result]