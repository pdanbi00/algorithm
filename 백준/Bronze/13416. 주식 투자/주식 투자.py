import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        tmp = max(a, b, c)
        if tmp < 0:
            continue
        answer += tmp

    print(answer)