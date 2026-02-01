info = dict()
for i in range(1, 10):
    a, b, c = input().split()
    info[i] = [a, b, c]

answer = set()
# 가능한 합 모두 찾기
for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(j+1, 10):
            possible = True
            for p in range(3):
                if (info[i][p] == info[j][p] and info[j][p] == info[k][p]) or (info[i][p] != info[j][p] and info[j][p] != info[k][p] and info[k][p] != info[i][p]):
                    continue
                else:
                    possible = False
                    break

            if possible:
                answer.add((i, j, k))

# print(answer)

score = 0
N = int(input())
used = set()
g_used = False
for _ in range(N):
    d = list(input().split())
    if d[0] == 'G':
        if not g_used and len(used) == len(answer):
            score += 3
            g_used = True

        else:
            score -= 1
        # print(score)
    else:
        result = sorted(d[1:])
        a, b, c = int(result[0]), int(result[1]), int(result[2])

        if (a, b, c) in answer and (a, b, c) not in used:
            score += 1
            used.add((a, b, c))
        else:
            score -= 1
        # print(score)

print(score)