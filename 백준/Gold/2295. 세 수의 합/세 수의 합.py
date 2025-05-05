# x + y + z = k -> x + y = k - z

N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)

nums.sort()
nums_sum = set()
for n1 in nums:
    for n2 in nums:
        nums_sum.add(n1+n2)

def check():
    global answer
    for i in range(N-1, -1, -1):
        for j in range(i+1): # z랑 k랑 같은 수여도 되니깐 i번째 인덱스도 가능. i이상의 인덱스일 경우 값이 음수 일 수 있는데 k는 자연수이니깐 최대 i까지만
            if nums[i] - nums[j] in nums_sum:
                answer = nums[i]
                return

answer = 0
check()
print(answer)