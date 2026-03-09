# 30의 배수 찾는 법 -> 3의 배수이면서 10의 배수
# 10의 배수 -> 마지막 자리는 무조건 0
# 3의 배수 -> 각 자리 수의 합이 3의 배수이면 됨

N = list(input())

N.sort(reverse=True)
possible = True

if N[-1] != '0':
    possible = False
else:
    total = 0
    for i in range(len(N)):
        total += int(N[i])
    if total % 3 != 0:
        possible = False

if possible:
    print(int(''.join(N)))
else:
    print(-1)