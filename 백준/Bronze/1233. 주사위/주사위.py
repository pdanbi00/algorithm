S1, S2, S3 = map(int, input().split())
cnt = dict()
answer = 0

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            tmp = i + j + k

            if tmp in cnt:
                cnt[tmp] += 1
            else:
                cnt[tmp] = 1
            answer = max(answer, cnt[tmp])

arr = []
for k, v in cnt.items():
    if v == answer:
        arr.append(k)

arr.sort()
print(arr[0])