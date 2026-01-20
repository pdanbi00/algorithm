s = ['A', 'B', 'C']
c = ['B', 'A', 'B', 'C']
h = ['C', 'C', 'A', 'A', 'B', 'B']

N = int(input())
answer = input()

s_score = 0
c_score = 0
h_score = 0

for i in range(N):
    if answer[i] == s[i%3]:
        s_score += 1
    if answer[i] == c[i%4]:
        c_score += 1
    if answer[i] == h[i%6]:
        h_score += 1


max_score = max(s_score, c_score, h_score)

answer = []
if s_score == max_score:
    answer.append('Adrian')
if c_score == max_score:
    answer.append("Bruno")
if h_score == max_score:
    answer.append("Goran")

print(max_score)
for i in range(len(answer)):
    print(answer[i])