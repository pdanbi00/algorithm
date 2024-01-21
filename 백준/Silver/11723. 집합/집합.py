import sys
input = sys.stdin.readline
n = 20
m = int(input())
s = 0
for _ in range(m):
    op, *num = input().split() # 이렇게 하면 띄워쓰기 뒤에 뭐가 더 있으면 ['10'] 이런식으로 되고 없으면 [] 이렇게 됨.
    if len(num) > 0:
        x = int(num[0]) - 1 # 숫자는 1부터 20까지 있으니깐 비트마스크로는 0부터 확인하니깐 1 빼기
    if op == 'add':
        s = (s | (1 << x))
    elif op == 'remove':
        s = (s & ~(1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        if res > 0:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        s = (s ^ (1 << x))
    elif op == 'all':
        s = (1 << 20) - 1
    else:
        s = 0