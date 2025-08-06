arr = list(input())
idx = 1
answer = 10
pre = arr[0]
while idx < len(arr):
    if arr[idx] == pre:
        answer += 5
        idx += 1
    else:
        answer += 10
        pre = arr[idx]
        idx += 1
print(answer)