nums = []
cnt = 0
l = 0
while True:
    num = list(input().split())
    if cnt == 0:
        cnt = int(num[0])
        arr = num[1:]
        for a in arr:
            nums.append(int(a[::-1]))
        l += len(arr)
    else:
        arr = num[:]
        for a in arr:
            nums.append(int(a[::-1]))
        l += len(num)
    if l == cnt:
        break
nums.sort()
for n in nums:
    print(n)