# 이거는 재귀다
def solution(arr):
    answer = [0] * 2
    func(0, 0, len(arr), arr, answer)
    return answer

def func(r, c, k, arr, answer):
    if k == 1:
        answer[arr[r][c]] += 1
        return
    
    # 우선 r, c 부터 r+k, c+k까지 모두 같은 수인지 확인
    possible = True
    target = arr[r][c]
    for i in range(k):
        for j in range(k):
            if arr[r+i][c+j] != target:
                possible = False
                break
        if not possible:
            break
    
    if possible:
        answer[target] += 1
        return
    
    func(r, c, k//2, arr, answer)
    func(r+(k//2), c, k//2, arr, answer)
    func(r, c+(k//2), k//2, arr, answer)
    func(r+(k//2), c+(k//2), k//2, arr, answer)
    