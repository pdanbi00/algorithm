
from itertools import permutations
N = int(input())
nums = [i for i in range(1, N+1)]
for perm in permutations(nums, N):
    print(' '.join(map(str, list(perm))))