# # bfs
# # 각 여행 계획지별로 A, B, C 순서라면 A, B까지 갈 수 있는지 bfs, B에서 C까지 갈 수 있는지 각각 bfs실행
# from collections import deque
# N = int(input())
# M = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# route = list(map(int, input().split()))
#
#
# def bfs(start, end):
#     visitied = [0] * N
#     q = deque()
#     q.append(start)
#     visitied[start] = 1
#     while q:
#         idx = q.popleft()
#         if idx == end:
#             return True
#
#         for k in range(N):
#             if board[idx][k] == 1 and visitied[k] == 0:
#                 q.append(k)
#                 visitied[k] = 1
#     # 다음 여행지로 못가는 경우
#     return False
#
# ans = "YES"
# for i in range(M-1):
#     possible = bfs(route[i]-1, route[i+1]-1)
#     if not possible:
#         ans = "NO"
#         break
# print(ans)
#
# Union Find
# 특정 정점부터 특정 정점까지 이어져있는지 확인할 수 있다.

# 노드 합치기
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 부모 노드 찾기
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
M = int(input())
parents = [i for i in range(N)]

for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j)
path = list(map(int, input().split()))
for i in range(M-1):
    if parents[path[i]-1] != parents[path[i+1]-1]:
        print("NO")
        break
else:
    print("YES")