N, P, Q = map(int, input().split())

dict = {}
dict[0] = 1

def solution(n):
    # n번째 값이 저장되어 있다면 그대로 반환
    if n in dict:
        return dict[n]
    # 저장되어 있지 않다면 n번째 값 계산 및 저장 후 반환
    else:
        dict[n] = solution(n//P) + solution(n//Q)
        return dict[n]

print(solution(N))