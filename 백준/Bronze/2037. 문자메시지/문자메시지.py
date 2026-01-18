p, w  = map(int, input().split())
time = 0
line = input()
L = len(line)

nums = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
pre = -1
for a in line:
    if a == ' ':
        time += p
        pre = -1
    else:
        for i in range(8):
            if a in nums[i]:
                if i == pre:
                    time += w
                else:
                    pre = i
                break
        for j in range(len(nums[i])):
            if a == nums[i][j]:
                time += p * (j+1)

print(time)