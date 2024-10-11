line = input()
bomb = input()

# stack으로 문자열 폭발 구현
stack = []
N = len(bomb)

for i in range(len(line)):
    stack.append(line[i])
    if ''.join(stack[-N:]) == bomb:
        for _ in range(N):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')