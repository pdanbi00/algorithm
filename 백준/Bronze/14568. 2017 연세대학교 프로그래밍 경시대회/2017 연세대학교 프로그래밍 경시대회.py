N = int(input())

# n = y + k
# t % 2 = 0

# N - t = y + y + k
# 2y : tmp - k

answer = set()
for a in range(2, N-1, 2):
    tmp = N - a
    for k in range(2, tmp):
        if (tmp - k) % 2 == 0:
            b = (tmp - k) // 2
            if b > 0:
                c = b + k
                answer.add((a, b, c))

print(len(answer))