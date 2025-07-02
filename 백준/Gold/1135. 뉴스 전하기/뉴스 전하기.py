N = int(input())
parent_list = list(map(int, input().split()))
child_list = [[] for _ in range(N)]

for i in range(1, N):
    child_list[parent_list[i]].append(i)
def dfs(node):
    if not child_list[node]:
        return 0

    result = []
    for child in child_list[node]:
        result.append(dfs(child))
    result.sort(reverse=True)
    new_result = []
    for i in range(len(child_list[node])):
        new_result.append(result[i] + i + 1)
    return max(new_result)

print(dfs(0))