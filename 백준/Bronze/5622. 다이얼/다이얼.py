nums = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ans = 0
word = input()
for w in word:
    for i in range(len(nums)):
        if w in nums[i]:
            ans += i + 3
print(ans)