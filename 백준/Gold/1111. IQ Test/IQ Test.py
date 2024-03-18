# N이 1이면 B
# N이 2이면 숫자 두개가 같으면 그 숫자 출력, 숫자가 다르면 B 출력
# 숫자 3개 이상부터 판단.
N = int(input())
nums = list(map(int, input().split()))
ans_list = [[] for _ in range(N-1)]
if N == 1:
    print('A')
elif N == 2:
    if nums[0] == nums[1]:
        ans = nums[0]
    else:
        ans = 'A'
    print(ans)
else:
    if nums[0] - nums[1] == 0:
        a = 0
    else:
        a = (nums[1] - nums[2]) // (nums[0] - nums[1])
    b = nums[1] - (nums[0] * a)
    for i in range(N-1):
        expect = nums[i]*a + b # 다음 예상값
        if expect != nums[i+1]:
            print('B')
            exit()
    print(nums[-1]*a + b)