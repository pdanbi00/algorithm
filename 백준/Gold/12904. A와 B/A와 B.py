from collections import deque
S = list(input())
T = list(input())

q = deque()
visited = set()
possible = True
q.append(tuple(T))
visited.add(tuple(T))

while q:
    arr = q.popleft()
    if arr == S:
        print(1)
        exit()
    arr = list(arr)
    tmp = arr.pop()
    if arr:
        if tmp == 'A':
            q.append(arr)
        else:
            q.append(arr[::-1])

print(0)