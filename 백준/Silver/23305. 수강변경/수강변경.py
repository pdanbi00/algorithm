N = int(input())
have = list(map(int, input().split()))
want = list(map(int, input().split()))

data = [0] * 1000001

for i in have:
    data[i] += 1

answer = 0
for i in want:
    if data[i] > 0:
        data[i] -= 1
    else:
        answer += 1
print(answer)