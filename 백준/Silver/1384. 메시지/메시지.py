from collections import deque
tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    cnt = 0
    names = deque()
    messages = []
    for _ in range(N):
        arr = list(input().split())
        names.append(arr[0])
        messages.append(arr[1:])
    bad = []
    for i in range(N):
        tmp = names[0]
        for j in range(N-1):
            name = names.pop()
            if messages[i][j] == 'N':
                cnt += 1
                bad.append((name, tmp))
            names.appendleft(name)
    print(f'Group {tc}')
    if cnt == 0:
        print("Nobody was nasty")
    else:
        for a, b in bad:
            print(f'{a} was nasty about {b}')
    print()
