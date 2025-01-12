total = int(input())
N = int(input())
ans = 0
for _ in range(N):
    cost, size = map(int, input().split())
    tmp = cost * size
    ans += tmp
    
if total == ans:
    print('Yes')
else:
    print("No")