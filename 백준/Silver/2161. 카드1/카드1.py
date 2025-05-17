N = int(input())

cards = [i for i in range(1, N+1)]

while cards:
    print(cards.pop(0), end = " ")
    if cards:
        tmp = cards.pop(0)
        cards.append(tmp)