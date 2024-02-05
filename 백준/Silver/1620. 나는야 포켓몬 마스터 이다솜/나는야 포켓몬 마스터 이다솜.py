import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pocketmon = {}
for i in range(1, N+1):
    name = input().strip()
    pocketmon[name] = i
    pocketmon[i] = name

for n in range(M):
    a = input().strip()
    if a.isdigit():
        print(pocketmon[int(a)])
    else:
        print(pocketmon[a])