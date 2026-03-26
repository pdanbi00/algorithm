import sys
input = sys.stdin.readline
N = int(input())
dots_x = dict()
x_set = set()
for _ in range(N):
    x, y = map(int, input().split())
    x_set.add(x)
    if x not in dots_x:
        dots_x[x] = [y]
    else:
        dots_x[x].append(y)

answer = 0

x_set = list(x_set)
x_set.sort()
n = len(x_set)
for i in range(n):
    for j in range(i+1, n):
        for y1 in dots_x[x_set[i]]:
            for y2 in dots_x[x_set[j]]:
                if y1 < y2:
                    if y2 in dots_x[x_set[i]] and y1 in dots_x[x_set[j]]:
                        answer += 1

print(answer)