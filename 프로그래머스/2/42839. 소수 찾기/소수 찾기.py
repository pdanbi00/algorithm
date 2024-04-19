from itertools import permutations
from math import sqrt
def check_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(numbers):
    # 순열로 모든 숫자 겨우 다 구해서 각각 소수인지 판단
    prime_nums = set()
    answer = 0
    for i in range(1, len(numbers)+1):
        for nums in permutations(numbers, i):
            prime_nums.add(int(''.join(nums)))
    arr = list(prime_nums)
    for a in arr:
        if check_prime(a):
            answer += 1
    return answer