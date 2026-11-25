import math
M = int(input())
N = int(input())

min = N+1
total = 0
for i in range(M, N+1):
    num = int(math.sqrt(i))
    tmp = num * num
    if tmp == i:
        total += tmp
        if min == N+1:
            min = tmp

if total == 0:
    print(-1)
else:
    print(total)
    print(min)