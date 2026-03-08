import sys
input = sys.stdin.readline

while True:
    N = input().rstrip()
    cnt = 0
    zero = 0

    if N == '0':
        break
    elif N == N[::-1]:
        print(cnt)
        continue
    else:
        tmp = len(N)
        while N != N[::-1]:
            cnt += 1
            t = int(N) + 1
            N = str(t).zfill(tmp)
        print(cnt)
