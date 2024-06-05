from itertools import permutations
N = int(input())
nums = list(map(int, input().split()))
buho_cnt = list(map(int, input().split()))
buho_list = ['+', '-', '*', '/']
buho = []

for i in range(4):
    for j in range(buho_cnt[i]):
        buho.append(buho_list[i])

min_ans = 1000000000
max_ans = -1000000000

cases = set()

for p in permutations(buho, N-1):
    cases.add(p)

def solve():
    global min_ans, max_ans
    for case in cases:
        total = nums[0]
        for i in range(1, N):
            if case[i-1] == '+':
                total += nums[i]
            elif case[i-1] == '-':
                total -= nums[i]
            elif case[i-1] == '*':
                total *= nums[i]
            elif case[i-1] == '/':
                if total < 0 and nums[i] > 0:
                    total = -(abs(total) // nums[i])
                else:
                    total = total // nums[i]
        if total > max_ans:
            max_ans = total
        if total < min_ans:
            min_ans = total

solve()
print(max_ans)
print(min_ans)