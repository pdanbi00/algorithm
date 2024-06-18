import sys
input = sys.stdin.readline
arr = []

N = int(input())
for _ in range(N):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    arr.append((korean, english, math, name))
arr.sort(key=lambda x : (-x[0], x[1], -x[2], x[3]))
for i in range(N):
    print(arr[i][3])