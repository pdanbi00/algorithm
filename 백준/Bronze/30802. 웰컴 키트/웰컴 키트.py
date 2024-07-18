N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t_shirt = 0
pen_big = 0
pen_small = 0

for s in sizes:
    if s % T == 0:
        t_shirt += (s // T)
    else:
        t_shirt += (s // T) + 1

pen_big += N // P
pen_small += N % P

print(t_shirt)
print(pen_big, pen_small)