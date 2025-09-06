import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    G = int(input())
    students = [int(input()) for _ in range(G)]

    if G == 1:
        print(1)
    else:
        cnt = 2
        while True:
            mod = set()
            for i in range(G):
                mod.add(students[i] % cnt)
            mod = list(mod)
            if len(mod) == G:
                print(cnt)
                break
            else:
                cnt += 1