word1 = input()
word2 = input()

ans = 0

dict = {}

for w in word1:
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1

for w in word2:
    if w in dict:
        if dict[w] > 0:
            dict[w] -= 1
        else:
            ans += 1
    else:
        ans += 1

for k, v in dict.items():
    if v > 0:
        ans += v

print(ans)