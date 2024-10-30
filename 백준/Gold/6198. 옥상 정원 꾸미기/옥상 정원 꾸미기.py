# 아이디어 : 내가 볼 수 있는 옥상의 수가 아니라 나를 볼 수 있는 관리인의 수를 구해야 됨.
N = int(input())
ans = 0
stack = []
buildings = [int(input()) for _ in range(N)]

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop() # 옥상을 볼 수 없는 관리인은 전부 제거

    ans += len(stack) # 옥상을 볼 수 있는 관리인 수
    stack.append(building) # 지금 빌딩 스택에 추가

print(ans)