chang = 100
sang = 100

N = int(input())
for _ in range(N):
    c, s = map(int, input().split())
    if c < s:
        chang -= s
    elif c > s:
        sang -= c

print(chang)
print(sang)