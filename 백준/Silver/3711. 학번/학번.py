import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    G = int(input())
    students = [int(input()) for _ in range(G)]

    if G == 1:
        print(1)
    else:
        maxS = max(students)
        used = [-1] * (maxS + 1)
        for i in range(2, maxS+2):
            roundId = i-1
            possible = True
            for j in range(G):
                m = students[j] % i
                if used[m] == roundId:
                    possible = False
                    break
                else:
                    used[m] = roundId

            if possible:
                print(i)
                break