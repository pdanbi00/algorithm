N, L = map(int, input().split())

signal = []
time = 0
dist = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    signal.append((D, R, G))
    time += D - dist
    dist = D
    if time % (R+G) < R:
        time += R - (time % (R+G))
    else:
        continue

time += L - dist
print(time)