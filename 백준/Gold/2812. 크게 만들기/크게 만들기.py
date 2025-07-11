N, K = map(int, input().split())
num = list(input())
stack = []
idx = 0
while idx < N:
    while stack:
        if stack[-1] < num[idx]:
            stack.pop()
            K -= 1
            if K == 0:
                break
        else:
            break
    if K == 0:
        break
    stack.append(num[idx])
    idx += 1

while idx < N:
    stack.append(num[idx])
    idx += 1

while K > 0:
    stack.pop()
    K -= 1

print(''.join(map(str, stack)))

'''
6 2
999899
'''