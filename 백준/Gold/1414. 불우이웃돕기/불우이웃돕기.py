# 랜선길이 다 더해서 최소거리 빼고 출력
# 크루스칼(엣지 관점임)
# 소문자면 ord 해서 -96
# 대문자면 ord 해서 -38

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
board = [list(input()) for _ in range(N)]
parents = [i for i in range(N)]
total = 0
edge = []
# 문자 숫자로 변환
for i in range(N):
    for j in range(N):
        if board[i][j] in small:
            board[i][j] = ord(board[i][j]) - 96
        elif board[i][j] in big:
            board[i][j] = ord(board[i][j]) - 38
        else:
            board[i][j] = int(board[i][j])
        edge.append((board[i][j], i, j))
        total += board[i][j]
edge.sort()

for value, x1, x2 in edge:
    if value == 0:
        continue
    if find(x1) != find(x2):
        union(x1, x2)
        total -= value # 모든 전선 길이 다 더해서 최소로 필요한거만 뺴고 다 기부하면 됨.

check = set()
for i in range(N):
    if find(i) not in check:
        check.add(find(i)) # 이 과정을 해줘야 최종적으로 부모 노드를 찾아서 비교가 가능함.
if len(check) == 1: # 모든 컴퓨터가 하나의 네트워크로 연결됨
    print(total)
else:
    print(-1)