import sys
input = sys.stdin.readline
N = int(input())
num_dict = {}
new_num_list = []
nums_list = []
for i in range(N):
    n = int(input())
    nums_list.append(n)
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1
nums_list.sort()
for key, value in num_dict.items():
    new_num_list.append((key, value))
new_num_list.sort(key=lambda x : x[0])
new_num_list.sort(key=lambda x : x[1], reverse=True)

first = int(round(sum(nums_list) / len(nums_list), 0)) # 산술평균
second = nums_list[len(nums_list)//2] # 증가하는 순으로 했을 때 중앙값
if len(nums_list) == 1:
    third = new_num_list[0][0] # 최빈값
else:
    if new_num_list[0][1] == new_num_list[1][1]:
        third = new_num_list[1][0]
    else:
        third = new_num_list[0][0]
fourth = max(nums_list) - min(nums_list) # 최대값 - 최소값
print(first)
print(second)
print(third)
print(fourth)
