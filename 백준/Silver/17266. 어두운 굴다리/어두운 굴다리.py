N = int(input())
M = int(input())
lights = list(map(int, input().split()))

ans = -1
if len(lights) >= 2:
    for i in range(len(lights) - 1):
        dis = (lights[i+1] - lights[i]) // 2
        if (lights[i+1] - lights[i]) % 2 == 1:
            dis += 1
        ans = max(ans, dis)
front = lights[0] - 0
ans = max(ans, front)
back = N - lights[-1]
ans = max(ans, back)
print(ans)