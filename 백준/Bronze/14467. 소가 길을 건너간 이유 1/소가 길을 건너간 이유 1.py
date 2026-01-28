cow = [-1] * 11
answer = 0
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if cow[a] == -1:
        cow[a] = b
    else:
        if cow[a] != b:
            answer += 1
            cow[a] = b

print(answer)