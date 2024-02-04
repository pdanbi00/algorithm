N = int(input())
N_nums = list(map(int, input().split()))
dict = {}
for num in N_nums:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

M = int(input())
M_nums = list(map(int, input().split()))
for num in M_nums:
    if num not in dict:
        print(0, end=' ')
    else:
        print(dict[num], end=' ')