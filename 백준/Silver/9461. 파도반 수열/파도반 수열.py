trangles = [0] * 101

trangles[1] = 1
trangles[2] = 1
trangles[3] = 1

for i in range(4, 101):
    trangles[i] = trangles[i-3] + trangles[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(trangles[N])