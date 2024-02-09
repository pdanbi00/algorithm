from collections import deque

T = int(input())
for t in range(T):
    func = input()
    n = int(input())
    nums = input()[1:-1].split(',')

    q = deque(nums)
    if n == 0:
        q = []
    reverse_count = 0
    for f in func:
        if f == 'D':
            if len(q) >= 1:
                if reverse_count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                break
        elif f == 'R':
            reverse_count += 1
    else:
        if reverse_count % 2 == 0:
            print("["+','.join(q)+"]")
        else:
            # 남아있는 배열이 뒤집힌 상태니깐 배열 뒤집어줘야 됨
            q.reverse()
            print("["+','.join(q)+"]")