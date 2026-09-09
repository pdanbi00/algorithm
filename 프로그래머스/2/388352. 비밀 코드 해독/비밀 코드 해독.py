num_set = set()
def solution(n, q, ans):
    global num_set
    used = [False] * (n+1)
    func(0, 1, used, [], q, n, ans)
    return len(num_set)

def func(depth, idx, used, nums, q, n, ans):
    global num_set
    
    if depth == 5:
        for i in range(len(q)):
            tmp = 0
            for j in range(5):
                if nums[j] in q[i]:
                    tmp += 1
            if tmp != ans[i]:
                return
        num_set.add(tuple(nums))
        return
    
    else:
        for i in range(idx, n+1):
            if not used[i]:
                used[i] = True
                func(depth+1, i+1, used, nums + [i], q, n, ans)
                used[i] = False
        