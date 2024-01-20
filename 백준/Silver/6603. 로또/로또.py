from itertools import combinations

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    N = line[0]
    nums = line[1:]
    for num_com in combinations(nums, 6):
        print(' '.join(map(str,num_com)))
    print()
