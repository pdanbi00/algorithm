word = input()
answer = ''
for w in word:
    if w in "CAMBRIDGE":
        continue
    answer += w

print(answer)