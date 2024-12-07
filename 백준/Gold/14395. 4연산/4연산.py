from collections import deque
s, t = map(int, input().split())
q = deque()
q.append((s, ''))
visited = set() # 방문값을 저장해줄 set
visited.add(s)
find = False
if s == t:
    print(0)
elif t == 1:
    # t가 1일 경우는 나누기를 1번만 하면 됨
    print('/')
else:
    while q:
        num, calc = q.popleft()
        if num == t:
            print(calc)
            break
        if num ** 2 <= 10 ** 9 and num ** 2 not in visited:
            q.append((num * num, calc + '*'))
            visited.add(num * num)
        if num + num <= 10 ** 9 and num + num not in visited:
            q.append((num + num, calc + '+'))
            visited.add(num + num)
        # -는 연산 안함. 어차피 0 되니깐
        if num // num not in visited:
            q.append((num // num, calc + '/'))
    else:
        print(-1)