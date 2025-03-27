# 삭제하는 노드는 parent값을 -2로 바꾸기

N = int(input())
parents = list(map(int, input().split()))
delete = int(input())

def dfs(node, parents):
    parents[node] = -2
    for i in range(N):
        if parents[i] == node:
            dfs(i, parents)

dfs(delete, parents)
cnt = 0
for i in range(N):
    if parents[i] != -2 and i not in parents: # 삭제하는 노드의 자식 노드가 아니고, 어떤 노드의 부모 노드가 아닌 경우
        cnt += 1

print(cnt)