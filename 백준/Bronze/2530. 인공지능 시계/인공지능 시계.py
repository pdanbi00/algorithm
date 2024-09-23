H, M, S = map(int, input().split())
time = 0
time += H * 60 * 60
time += M * 60
time += S

D = int(input())
time += D

while time >= 24 * 60 * 60:
    time -= 24 * 60 * 60
H = time // (60 * 60)
time -= (H * 60 * 60)
M = time // 60
time -= (M * 60)
S = time
print(H, M, S)