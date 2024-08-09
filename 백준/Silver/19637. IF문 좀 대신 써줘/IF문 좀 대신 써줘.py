# 이분탐색...

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

power_arr = []
for i in range(N):
    status, num = input().split()
    power_arr.append((status, num))
power_arr.sort(key=lambda x : int(x[1]))

for _ in range(M):
    po = int(input())

    start = 0
    end = N
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if int(power_arr[mid][1]) >= po:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(power_arr[result][0])
