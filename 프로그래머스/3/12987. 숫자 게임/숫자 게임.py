def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    N = len(A)
    a = 0
    b = 0
    # 현재 배열에서 가장 큰 값끼리 비교
    while N > 0:
        # B가 더 크다면 두 배열의 최대값을 없애고 승점 +1
        if A[a] < B[b]:
            b += 1
            answer += 1
        # 만약 작다면 B의 최대값은 A의 다른 작은 값과 비교하기 위해서 두고 B의 최소값으로 패배한다고 생각하고 A는 넘기고 B는 둠
        a += 1
        N -= 1
    
    return answer