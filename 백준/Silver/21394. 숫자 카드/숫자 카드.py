from collections import deque
T = int(input())
for _ in range(T):
    cards_cnt = list(map(int, input().split()))
    cards = deque()
    for i in range(9):
        if i == 5:
            continue
        for j in range(cards_cnt[i]):
            cards.append(i+1)
    for j in range(cards_cnt[5]):
        cards.append(9)

    left = deque()
    right = deque()

    idx = 0
    while cards:
        if idx % 2 == 0:
            left.append(cards.pop())
        else:
            right.appendleft(cards.pop())
        idx += 1

    answer = left + right
    print(*answer)