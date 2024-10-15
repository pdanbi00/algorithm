# 스택...
# 양쪽을 살펴봐야하기 때문에 하나는 처음부터 끝까지 진행.
# 하나는 끝에서부터 처음까지 진행하면서 계산
N = int(input())
bildings = list(map(int, input().split()))

total = [0] * N

front = [[0] * 2 for _ in range(N)]
# 건물의 왼쪽들 살펴보기
stack = [(bildings[0], 0)]
for i in range(1, N):
    while stack and stack[-1][0] <= bildings[i]:
        stack.pop()
    if stack:
        front[i][0] = stack[-1][0]
        front[i][1] = stack[-1][1]
    total[i] += len(stack)
    stack.append((bildings[i], i))

back = [[0] * 2 for _ in range(N)]
# 건물의 오른쪽들 살펴보기
stack = [(bildings[-1], N-1)]
for i in range(N-2, -1, -1):
    while stack and stack[-1][0] <= bildings[i]:
        stack.pop()
    if stack:
        back[i][0] = stack[-1][0]
        back[i][1] = stack[-1][1]
    total[i] += len(stack)
    stack.append((bildings[i], i))

for i in range(N):
    if front[i] != [0, 0] and back[i] != [0, 0]:
        if i - front[i][1] <= back[i][1] - i:
            print(total[i], front[i][1]+1)
        else:
            print(total[i], back[i][1]+1)
    elif front[i] != [0, 0]:
        print(total[i], front[i][1]+1)
    elif back[i] != [0, 0]:
        print(total[i], back[i][1]+1)
    else:
        print(0)