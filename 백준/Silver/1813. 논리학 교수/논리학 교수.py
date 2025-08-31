N = int(input())
arr = list(map(int, input().split()))
info = dict()
max_k = 0
for i in range(N):
    max_k = max(max_k, arr[i])
    if arr[i] in info:
        info[arr[i]] += 1
    else:
        info[arr[i]] = 1

answer = 0

for k, v in info.items():
    if k == v and k >= answer:
        answer = k

if answer == 0 and 0 in info:
    answer = -1

print(answer)