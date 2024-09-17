# 슬라이딩 윈도우
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
blog = list(map(int, input().split()))

tmp = sum(blog[:X])
max_v = tmp
cnt = 1
for i in range(X, N):
    tmp -= blog[i-X]
    tmp += blog[i]
    if max_v < tmp:
        max_v = tmp
        cnt = 1
    elif max_v == tmp:
        cnt += 1
if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)