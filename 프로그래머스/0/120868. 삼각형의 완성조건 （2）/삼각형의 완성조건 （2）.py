def solution(sides):
    answer = 0
    tmp = set()
    mx = max(sides)
    mi = min(sides)
    # 1. sides 중 제일 큰 값이 제일 긴 변인 경우
    for i in range(1, mx):
        if i + mi > mx:
            tmp.add(i)
            
    # 2. 아직 결정 안 된 값이 제일 긴 변인 경우
    for i in range(mx, mx+mi):
        if i < mx+mi:
            tmp.add(i)
    return len(tmp)