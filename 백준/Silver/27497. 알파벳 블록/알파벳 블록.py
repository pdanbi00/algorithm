from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
ans = deque()
front = [] # 블록이 앞에 추가됐는지 뒤에 추가됐는지
for _ in range(N):
    command = input().rstrip().split()
    if command[0] == '3':
        if ans:
            if front.pop(): # 마지막으로 추가된 블록이 앞이라면
                ans.popleft()
            else:
                ans.pop()
    elif command[0] == '1': # 뒤에 추가하는 경우
        ans.append(command[1])
        front.append(False)
    else:
        ans.appendleft(command[1])
        front.append(True)

s = list(ans)
if s:
    print(''.join(s))
else:
    print(0)