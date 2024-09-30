# 스택 문제
# 
# 높이가 스택 마지막 값보다 큰 경우
# - 새로운 건물이니깐 갯수 1 증가
# 높이가 스택 마지막 값보다 작고, 해당 높이가 존재하지 않는 경우
# - 새로운 건물이니깐 갯수 1 증가
# - 그 값이 스택에서 가장 큰 값이 되도록 pop
# 높이가 스택 마지막 값보다 작고, 해당 높이가 존재하는 경우
# - 기존에 있던 건물이니깐 갯수는 패스
# - 그 값이 스택에서 가장 큰 값이 되도록 pop

import sys
input = sys.stdin.readline

N = int(input())
stack = [0]
res = 0
for _ in range(N):
    x, y = map(int, input().split())
    if stack[-1] < y:
        res += 1
        stack.append(y)
    else:
        while stack[-1] > y:
            stack.pop()
            
        if stack[-1] != y:
            stack.append(y)
            res += 1
print(res)