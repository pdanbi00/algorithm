# 음수가 있으면 0이랑 묶어서 없애버리기
# 숫자들은 큰것들끼리 묶기
# 1은 최대한 더하는 방향으로
# 일단 숫자를 정렬시킴
# 0이하끼리 리스트 하나
# 0초과끼리 리스트 하나
# 우선 수열 개수가 1개면 그냥 출력
# 2개 이상부터 생각해야 됨
# 숫자들을 음수, 0, 양수 리스트에 나눠 담음
# 각 리스트들 정렬시킴
# 각 배열 개수 확인
# 이거도 1이면 그냥 하는데? 음수가 홀수개이면 절대값 큰거끼리 2개 씩 묶고 만약에 0 있으면 마지막 남는거 0이랑 묶고

import sys
input = sys.stdin.readline
minus = []
plus = []
zero = []
N = int(input())
if N == 1:
    print(int(input()))
else:
    ans = 0
    for i in range(N):
        num = int(input())
        if num > 0:
            plus.append(num)
        elif num == 0:
            zero.append(num)
        else:
            minus.append(num)
    plus.sort(reverse=True)
    minus.sort()
    # 음수가 짝수개이고 0개 이상이면 2개씩 묶어주면 됨
    if len(minus) % 2 == 0 and len(minus) > 0:
        for j in range(0, len(minus)-1, 2):
            ans += minus[j] * minus[j+1]
    # 음수가 홀수개이고 0개 이상이면 1개 빼고 2개씩 묶어주면 됨
    elif len(minus) % 2 == 1 and len(minus) > 0:
        for j in range(0, len(minus)-2, 2):
            ans += minus[j] * minus[j+1]
        if len(zero) == 0:
            ans += minus[-1]
    # 양수가 짝수개이고 0개 이상이면 2개씩 묶어주면 됨
    if len(plus) % 2 == 0 and len(plus) > 0:
        for j in range(0, len(plus) - 1, 2):
            if plus[j] == 1 or plus[j+1] == 1:
                ans += plus[j] + plus[j + 1]
            else:
                ans += plus[j] * plus[j + 1]
    # 양수가 홀수개이고 0개 이상이면 1개 빼고 2개씩 묶어주면 됨
    elif len(plus) % 2 == 1 and len(plus) > 0:
        for j in range(0, len(plus) - 2, 2):
            if plus[j] == 1 or plus[j + 1] == 1:
                ans += plus[j] + plus[j + 1]
            else:
                ans += plus[j] * plus[j + 1]
        ans += plus[-1]
    print(ans)
