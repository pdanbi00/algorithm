N, M, K = map(int, input().split())

used1 = [False] * N
nums = []
cnt1 = 0
cnt2 = 0
def find1(idx, i, num):
    global cnt1, nums
    if idx == M:
        cnt1 += 1
        nums.append(num)
        return

    for j in range(i, N):
        if not used1[j]:
            used1[j] = True
            find1(idx+1, j, num + str(j))
            used1[j] = False

find1(0, 0, '')

target = ''
for i in range(M):
    target += str(i)
total_cnt = 0
for num in nums:
    cnt = 0
    for i in range(M):
        if num[i] in target:
            cnt += 1
    if cnt >= K:
        total_cnt += 1
        
print(total_cnt / cnt1)