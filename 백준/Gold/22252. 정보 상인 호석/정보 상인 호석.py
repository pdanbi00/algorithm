import sys
import heapq
input = sys.stdin.readline

Q = int(input())
info = {}
ans = 0
for i in range(Q):
    kind, name, *cost = input().split()
    if kind == '1':
        if name in info:
            info[name].extend(list(map(int, cost[1:])))
        else:
            info[name] = list(map(int, cost[1:]))
        info[name].sort(reverse=True)
    else:
        if name in info.keys():
            if int(cost[0]) > len(info[name]):
                cost = len(info[name])
            else:
                cost = int(cost[0])

            for j in range(cost):
                ans += info[name].pop(0)
print(ans)