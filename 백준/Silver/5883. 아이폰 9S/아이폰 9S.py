N = int(input())
num_set = set()
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)
    num_set.add(num)

answer = 0
for i in num_set:
    pre = -1
    tmp = 0
    for j in range(N):
        if arr[j] == i:
            continue
        if arr[j] == pre:
            tmp += 1
        else:
            answer = max(answer, tmp)
            pre = arr[j]
            tmp = 1
    answer = max(answer, tmp)
print(answer)