N = int(input())
ans = []
for i in range(N):
    x, y = map(int,input().split())
    ans.append((x, y))
ans.sort(key=lambda x : (x[1], x[0]))
for i in range(N):
    print(ans[i][0], ans[i][1])
