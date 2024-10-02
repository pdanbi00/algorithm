def dfs(idx, total, numbers, target):
    global answer
    if idx == len(numbers):
        if total == target:
            answer += 1
        return
    dfs(idx+1, total + numbers[idx], numbers, target)
    dfs(idx+1, total - numbers[idx], numbers, target)
    
answer = 0
def solution(numbers, target):
    
    visited = [0] * len(numbers)
    dfs(0, 0, numbers, target)
    return answer