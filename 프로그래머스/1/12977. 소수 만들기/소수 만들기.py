import math
def solution(nums):
    answer = 0
    
    N = len(nums)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                tmp = nums[i] + nums[j] + nums[k]
                possible = True
                for p in range(2, int(math.sqrt(tmp)) + 1):
                    if tmp % p == 0:
                        possible = False
                        break
                        
                if possible:
                    answer += 1

    return answer