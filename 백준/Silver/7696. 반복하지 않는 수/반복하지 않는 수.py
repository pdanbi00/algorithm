from collections import deque
import sys
input = sys.stdin.readline
num = 1
nums = deque()

def duplication(num):
    check = [False] * 10
    while num > 0:
        tmp = num % 10
        if check[tmp]:
            return True
        check[tmp] = True
        num //= 10
    return False

while len(nums) < 1000000:
    if duplication(num) == False:
        nums.append(num)
    num += 1

while True:
    N = int(input())
    if N == 0:
        break
    print(nums[N-1])