T = int(input())
num = []
for _ in range(T):
    n = int(input())
    num.append(n)
num.sort()
for i in range(T):
    print(num[i])