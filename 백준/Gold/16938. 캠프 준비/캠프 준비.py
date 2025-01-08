N, L, R, X = map(int, input().split())
problem = sorted(list(map(int, input().split())))

ans = 0

# depth : 깊이. 즉, 몇개 선택 했는지
# idx : 조합을 위해서
# max_v : 선택한 수들 중 가장 큰 수. 정렬한 배열에서 고르기 때문에 가장 마지막에 선택된 수
# min_v : 선택한 수들 중 가장 작은 수. 정렬한 배열에서 고르기 때문에 가장 먼저 선택된 수
# total : 난이도 합
def dfs(depth, idx, max_v, min_v, total):
    global ans
    if total > R:
        return
    if depth >= 2 and L <= total <= R:
        if not (max_v == None or min_v == None) and max_v - min_v >= X:
            ans += 1

    for i in range(idx, len(problem)):
        # 최소가 없으면(depth == 0) 최소값 지정
        # 최소가 존재하면 최대값만 갱신
        if min_v == None:
            dfs(depth+1, i+1, problem[i], problem[i], total + problem[i])
        else:
            dfs(depth+1, i+1, problem[i], min_v, total + problem[i])

dfs(0, 0, None, None, 0)
print(ans)