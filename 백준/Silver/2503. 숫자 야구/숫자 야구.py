nums = []
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if i != k and j != k:
                tmp = i * 100 + j * 10 + k
                nums.append(str(tmp))

N = int(input())
num_cnt = [0] * len(nums)

for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = str(num)

    for i in range(len(nums)):
        n2 = nums[i]
        s = 0
        b = 0

        for j in range(3):
            if num[j] in n2:
                b += 1

            if num[j] == n2[j]:
                s += 1
                b -= 1
        if s == strike and b == ball:
            num_cnt[i] += 1

answer = 0
for i in range(len(num_cnt)):
    if num_cnt[i] == N:
        answer += 1

print(answer)