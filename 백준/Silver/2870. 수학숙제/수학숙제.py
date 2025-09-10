N = int(input())
nums = []
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for _ in range(N):
    line = input()
    idx = 0
    while idx < len(line):
        tmp = ''
        if line[idx] in num:
            tmp += line[idx]
            idx += 1
            while idx < len(line):
                if line[idx] in num:
                    tmp += line[idx]
                    idx += 1
                else:
                    break
            nums.append(int(tmp))
        idx += 1
nums.sort()
for i in range(len(nums)):
    print(nums[i])