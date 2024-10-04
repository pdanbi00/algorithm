# 스택을 2개를 사용함
# 커서를 기준으로 왼쪽에 위치한거랑 오른쪽에 위치한거 두개로 나눔
import sys

left = list(input())
right = []
M = int(input())
for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])
answer = left + list(reversed(right))
print(''.join(answer))