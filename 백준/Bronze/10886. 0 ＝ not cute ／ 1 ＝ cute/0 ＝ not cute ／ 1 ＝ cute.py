N = int(input())
y = 0
n = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        n += 1
    else:
        y += 1
        
if y > n:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')