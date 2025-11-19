from collections import deque
N = int(input())

first = deque(map(int, input().split()))
second = deque()
ans = []

# 원판 딕셔너리 만들어서 정보 입력
disk = dict()
for i in range(1, N+1):
    disk[i] = 1

for i in range(N, 0, -1):
    while True:
        if (disk[i] == 1 and first[-1] == i) or (disk[i] == 2 and second[-1] == i):
            if disk[i] == 1:
                first.pop()
                ans.append((1, 3))
            else:
                second.pop()
                ans.append((2, 3))
            break
        else:
            if disk[i] == 1:
                num = first.pop()
                disk[num] = 2
                second.append(num)
                ans.append((1, 2))
            else:
                num = second.pop()
                disk[num] = 1
                first.append(num)
                ans.append((2, 1))

print(len(ans))
for a, b in ans:
    print(a, b)