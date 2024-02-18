N = int(input())
num = [i for i in range(N+1)]
find = False
for i in range(1, N+1):
    n = i
    while n >= 10:
        num[i] += n // 10**(len(str(n))-1)
        n %= 10**(len(str(n))-1)
    num[i] += n
for i in range(N+1):
    if num[i] == N:
        find = True
        print(i)
        break
if find == False:
    print(0)