N, M = map(int, input().split())
J = int(input())

left = 1
right = M
move = 0

for _ in range(J):
    pos = int(input())
    if pos > right:
        diff = pos - right
        move += diff
        right = pos
        left += diff
    elif pos < left:
        diff = left - pos
        move += diff
        left = pos
        right -= diff

print(move)