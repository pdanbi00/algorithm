def solution(numbers):
    nums = set()
    N = len(numbers)
    for i in range(N-1):
        for j in range(i+1, N):
            nums.add(numbers[i] + numbers[j])
    return sorted(list(nums))