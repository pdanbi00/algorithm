scores = []
for i in range(5):
    s = int(input())
    if s < 40:
        s = 40
    scores.append(s)
print(sum(scores) // 5)