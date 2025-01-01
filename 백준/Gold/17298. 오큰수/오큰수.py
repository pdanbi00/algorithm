N = int(input())
arr = list(map(int, input().split()))

# 오큰수 저장할 배열
NGE = [-1] * N

stack = [0]
for i in range(1, N):
    # arr[i]가 이전의 수 들의 오큰수가 되는지 확인하기

    # 오큰수 : arr[i]의 오른쪽에 있으면서 arr[i]보다 큰 수 중 가장 왼쪽 값
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] =  arr[i]
    stack.append(i)

print(*NGE)