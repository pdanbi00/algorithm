K = int(input())
bu = input().split()
ans = []
checked = [False] * 10

def possible(x, y, op):
    if op == '>':
        if x < y:
            return False
    if op == '<':
        if x > y:
            return False
    return True

def func(index, nums):
    if index == K+1:
        ans.append(nums)
        return
    for i in range(10):
        if not checked[i]:
            if index == 0 or possible(nums[index-1], str(i), bu[index-1]):
                checked[i] = True
                func(index+1, nums+str(i))
                checked[i] = False
func(0, '')
print(max(ans))
print(min(ans))