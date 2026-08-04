def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1], -x[0]))
    nums = []
    n = len(data[0])
    for i in range(row_begin, row_end+1):
        tmp = 0
        for j in range(n):
            tmp += data[i-1][j] % i
        nums.append(tmp)
    answer = nums[0]
    for i in range(1, len(nums)):
        answer = answer ^ nums[i]
    return answer