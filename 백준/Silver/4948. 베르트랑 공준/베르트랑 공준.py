from math import sqrt
primeNum = []
for i in range(2, 123456*2 + 10):
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            break
    else:
        primeNum.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for num in primeNum:
        if n < num <= 2 * n:
            cnt += 1
        elif num > 2 * n:
            break
    print(cnt)