scores = [(int(input()), i + 1)for i in range(8)]
scores.sort(key=lambda x : (-x[0]))
total = 0
answer = []
for i in range(5):
    total += scores[i][0]
    answer.append(scores[i][1])
answer.sort()
print(total)
print(*answer)