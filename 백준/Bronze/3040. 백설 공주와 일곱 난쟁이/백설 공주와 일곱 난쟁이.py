from itertools import combinations
nums = []
for _ in range(9):
    num = int(input())
    nums.append(num)

for combi in combinations(nums, 7):
    if sum(combi) == 100:
        for n in combi:
            print(n)
        break