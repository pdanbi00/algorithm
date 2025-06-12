import sys
input = sys.stdin.readline
k = int(input())
A, B = map(int, input().split())
pizzaA = [int(input()) for _ in range(A)]
pizzaB = [int(input()) for _ in range(B)]

# 1. 각 피자에서 나올 수 있는 모든 경우의 수 탐색하기
def find_case(pizza):
    case = dict()
    for i in range(len(pizza)):
        tmp = pizza[i:] + pizza[:i]
        pre = 0
        for num in tmp:
            pre += num
            if pre not in case:
                case[pre] = 1
            else:
                case[pre] += 1
    case[sum(pizza)] = 1
    return case

case1 = find_case(pizzaA)
case2 = find_case(pizzaB)

answer = 0
if k in case1:
    # print('case1 : ', case1[k])
    answer += case1[k]
if k in case2:
    # print('case2 : ',case2[k])
    answer += case2[k]

for n1 in case1:
    n2 = k - n1
    if n2 in case2:
        # print(n1, n2, case1[n1] * case2[n2])
        answer += case1[n1] * case2[n2]

print(answer)