import sys
input = sys.stdin.readline
N = int(input())
cards = {}
for i in range(N):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1
card_arr = []
for k, v in cards.items():
    card_arr.append((k, v))
card_arr.sort()
card_arr.sort(key=lambda x : x[1], reverse=True)
print(card_arr[0][0])