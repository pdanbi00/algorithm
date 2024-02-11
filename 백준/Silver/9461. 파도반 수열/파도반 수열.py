trangles = [0] * 100
trangles[0] = 1
trangles[1] = 1
trangles[2] = 1
trangles[3] = 2
trangles[4] = 2
start = 0
end = 4
for i in range(5, 100):
    trangles[i] = trangles[start] + trangles[end]
    start += 1
    end += 1
T = int(input())
for _ in range(T):
    N = int(input())
    print(trangles[N-1])