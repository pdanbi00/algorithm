N = int(input())
cnt = 1
n = 0
if N >= 10:
    n = N // 10 + N % 10
    n = (N % 10) * 10 + (n % 10)
else:
    n = N * 11

while N != n:
    if n >= 10:
        temp = n
        n = temp // 10 + temp % 10
        n = (temp % 10) * 10 + (n % 10)
    else:
        n = n * 11
    cnt += 1
print(cnt)