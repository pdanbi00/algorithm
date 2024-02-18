from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int,input().split()))
    num_list = deque(num_list)
    find = M
    ans = 0
    while True:
        if num_list[0] == max(num_list):
            p = num_list.popleft()
            ans += 1
            if find == 0:
                print(ans)
                break
        else:
            num_list.append(num_list.popleft())
        find -= 1
        if find < 0:
            find = len(num_list) - 1