def calc(a, b):
    return a ** 2 - b ** 2

G = int(input())
a, b = 1, 1
ans = []

while a + b <= G:
    if calc(a, b) == G:
        ans.append(a)
        a += 1
    elif calc(a, b) > G:
        b += 1
    elif calc(a, b) < G:
        a += 1

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for a in ans:
        print(a)