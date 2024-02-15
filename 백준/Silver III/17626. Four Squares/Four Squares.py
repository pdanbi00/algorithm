# 완탐으로 풀기
# 풀이: 1. 일단 n이 제곱수이면 당연히 1 출력
#       2. 두 제곱수의 합으로 표현할 수 있다면 2 출력
#       (두 제곱수의 합을 저장하는 리스트를 따로 만들어두셈)
#       3. 제곱 수 리스트 돌면서 n - 제곱수 한 결과가 제곱수 합 리스트에 있으면 3 출력
#       n = (두 제곱수의 합) + (제곱수)인거니깐
#       4. 나머지 경우는 전부 4 출력. (모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 했으니깐 최대 4개)
from math import sqrt
from itertools import combinations_with_replacement
n = int(input())
square_nums = [i*i for i in range(1, int(sqrt(n))+1)] # 제곱수들 리스트
square_nums_sum = [sum(k) for k in combinations_with_replacement(square_nums, 2)] # 제곱수 2개 뽑은 합 리스트

def answer(n):
    if n in square_nums: # 제곱수이면
        return 1
    elif n in square_nums_sum: # 제곱수 2개 더해서 만들 수 있는 수이면
        return 2
    else:
        for num in square_nums: # 제곱수 중에
            if n - num in square_nums_sum: # n에서 제곱수를 뺀 수가 제곱수 두개를 더해서 만들 수 있는 수면
                return 3
    return 4

print(answer(n))