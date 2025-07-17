import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))
answer = []
if 0 not in A:
    answer = C
else:
    for i in range(N-1, -1, -1):
        if A [i]== 0:
            answer.append(B[i])
    answer.extend(C)
    # print(answer)
    answer = answer[:M]
print(*answer)