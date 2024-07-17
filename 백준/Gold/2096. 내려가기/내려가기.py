# DP인듯 하다
# 하지만 최대점수와 최소점수를 출력해야하기 때문에
# DP 테이블을 2개를 가져가자

import sys
input = sys.stdin.readline

N = int(input())

dp_max = [0] * 3
dp_min = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    if i == 0:
        dp_max[0], dp_max[1], dp_max[2] = a, b, c
        dp_min[0], dp_min[1], dp_min[2] = a, b, c
    else:
        tmp_a = max(dp_max[0], dp_max[1]) + a
        tmp_b = max(dp_max[0], dp_max[1], dp_max[2]) + b
        tmp_c = max(dp_max[1], dp_max[2]) + c
        dp_max[0] = tmp_a
        dp_max[1] = tmp_b
        dp_max[2] = tmp_c
        
        tmp_a = min(dp_min[0], dp_min[1]) + a
        tmp_b = min(dp_min[0], dp_min[1], dp_min[2]) + b
        tmp_c = min(dp_min[1], dp_min[2]) + c
        dp_min[0] = tmp_a
        dp_min[1] = tmp_b
        dp_min[2] = tmp_c
    
print(max(dp_max), min(dp_min))