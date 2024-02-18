import sys
input = sys.stdin.readline
N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
print(round(sum(num_list)/len(num_list))) # 산술평균
print(num_list[len(num_list)//2])# 중앙값

dict = {}
for i in num_list:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
max_num = max(dict.values())
max_dict = []
for i in dict: # 이러면 i는 딕셔너리의 key 값들이 됨
    if max_num == dict[i]:
        max_dict.append(i)
if len(max_dict) > 1:
    print(max_dict[1])
else:
    print(max_dict[0])
print(max(num_list) - min(num_list))