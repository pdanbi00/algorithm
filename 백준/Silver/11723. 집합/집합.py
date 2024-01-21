import sys
input = sys.stdin.readline

M = int(input())
ans = set()
for i in range(M):
    line = list(input().split())
    command = line[0]

    if command == 'add':
        ans.add(int(line[1]))
    elif command == 'remove':
        if int(line[1]) in ans:
            ans.remove(int(line[1]))
    elif command == 'check':
        if int(line[1]) in ans:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if int(line[1]) in ans:
            ans.remove(int(line[1]))
        else:
            ans.add(int(line[1]))
    elif command == 'all':
        ans = set([i for i in range(1, 21)])
    else:
        ans = set()

