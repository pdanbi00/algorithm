from collections import deque
T, A, B = map(int, input().split())

nums = set()
q = deque()
q.append((A, 0))
q.append((B, 0))
answer = 0
while q:
    value, used = q.popleft()
    answer = max(answer, value)
    tmp = value + A
    if tmp not in nums:
        if tmp <= T:
            if tmp == T:
                answer = T
                break
            else:
                q.append((tmp, used))
                nums.add(tmp)

    tmp = value + B
    if tmp not in nums:
        if tmp <= T:
            if tmp == T:
                answer = T
                break
            else:
                q.append((tmp, used))
                nums.add(tmp)
    if used == 0:
        tmp = value // 2
        if tmp not in nums:
            if tmp <= T:
                if tmp == T:
                    answer = T
                    break
                else:
                    q.append((tmp, 1))
                    nums.add(tmp)

print(answer)