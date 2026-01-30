N = int(input())
l = len(str(N))

cnt = 0
while True:
    N *= 2
    cnt += 1
    if len(str(N)) > l:
        break
print(cnt-1)