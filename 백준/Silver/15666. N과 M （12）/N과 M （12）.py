N, M = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))

seq = []
p = []
def solve(idx, depth):
    if depth == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(idx, len(nums)):
        seq.append(nums[i])
        solve(i, depth+1)
        seq.pop()

solve(0, 0)