X = int(input())
line = 1
# 몇번째 줄의 몇번째 숫자인지 구하기
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line + 1 - X
else:
    a = line + 1 - X
    b = X
print(a, '/', b, sep='')