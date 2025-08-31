N = int(input())
arr = list(map(int, input().split()))

answer = -1

for i in range(N+1):
    cnt = arr.count(i)
    if cnt == i:
        answer = max(answer, i)

print(answer)