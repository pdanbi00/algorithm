answer = [1, 1, 2, 2, 2, 8]

arr = list(map(int, input().split()))

for i in range(len(answer)):
    print(answer[i] - arr[i], end = " ")