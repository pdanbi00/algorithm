import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]
cnts = [0] * (d+1)
cnts[c] = 1

cnt = 1
for i in range(k):
    cnts[sushi[i]] += 1
    if cnts[sushi[i]] == 1:
        cnt += 1

answer = cnt

for start in range(N-1):
    cnts[sushi[start]] -= 1
    if cnts[sushi[start]] == 0:
        cnt -= 1

    idx = (start+k) % N
    cnts[sushi[idx]] += 1
    if cnts[sushi[idx]] == 1:
        cnt += 1

    answer = max(answer, cnt)

print(answer)