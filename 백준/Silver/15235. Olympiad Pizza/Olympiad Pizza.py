from collections import deque
N = int(input())
pizza = list(map(int, input().split()))
new_pizza = deque()
time = 0
for i in range(N):
    new_pizza.append((i, pizza[i]))

ans = [0] * N
while new_pizza:
    idx, cnt = new_pizza.popleft()
    time += 1
    if cnt-1 > 0:
        new_pizza.append((idx, cnt-1))
    else:
        ans[idx] = time
print(*ans)