N = int(input())
cards = list(map(int, input().split()))
answer = cards.copy()
answer.sort()

i = 1
op = 0
ch = []
while cards != answer:
    if cards[i-1] != i:
        op += 1
        k = cards.index(i) + 1
        cards[i-1:k] = cards[i-1:k][::-1]
        ch.append((i, k))
    i += 1
print(op)
for a, b in ch:
    print(a, b)