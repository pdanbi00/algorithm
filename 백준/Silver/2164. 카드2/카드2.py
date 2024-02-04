from collections import deque
N = int(input())
card = [i for i in range(1, N+1)]
card2 = deque(card)
while card2:
    if len(card2) == 1:
        print(card2.popleft())
        break
    card2.popleft()
    a = card2.popleft()
    card2.append(a)