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

    idx = 0
    answer = deque()
    if len(cards) % 2 == 1:
        while cards:
            if idx % 2 == 1:
                answer.append(cards.popleft())
            else:
                answer.appendleft(cards.popleft())
            idx += 1
    else:
        while cards:
            if idx % 2 == 0:
                answer.append(cards.popleft())
            else:
                answer.appendleft(cards.popleft())
            idx += 1

    print(*answer)