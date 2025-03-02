N = int(input())
nums = list(map(int, input().split()))
stack = []
idx = 1
for num in nums:
    # 대기열 한명 스택으로 보내기
    stack.append(num)
    # 보낼 수 있는지 확인하기
    # 스택이 비어있지 않다면 마지막 요소랑 현재 차례 비교
    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1

if stack:
    print("Sad")
else:
    print("Nice")