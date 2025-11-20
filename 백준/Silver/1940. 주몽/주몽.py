N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()
cnt = 0
s = 0
e = N-1

while s < e:
    total = materials[s] + materials[e]

    if total < M:
        s += 1
    elif total > M:
        e -= 1
    else:
        cnt += 1
        s += 1
        e -= 1
print(cnt)