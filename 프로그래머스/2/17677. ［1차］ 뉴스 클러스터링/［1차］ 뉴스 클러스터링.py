import math
def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()
    print(str1, str2)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    N1 = len(str1)
    N2 = len(str2)
    
    info_1 = dict()
    info_2 = dict()
    
    for i in range(N1-1):
        if str1[i] in alpha and str1[i+1] in alpha:
            tmp = str1[i] + str1[i+1]
            if tmp in info_1:
                info_1[tmp] += 1
            else:
                info_1[tmp] = 1
                
    for i in range(N2-1):
        if str2[i] in alpha and str2[i+1] in alpha:
            tmp = str2[i] + str2[i+1]
            if tmp in info_2:
                info_2[tmp] += 1
            else:
                info_2[tmp] = 1
    
    if not info_1 and not info_2:
        return 65536
    union = 0
    total = 0
    
    for k, v in info_1.items():
        if k in info_2:
            union += min(info_1[k], info_2[k])
            total += max(info_1[k], info_2[k])
        else:
            total += info_1[k]
            
    for k, v in info_2.items():
        if k not in info_1:
            total += info_2[k]
    answer = math.floor(union / total * 65536)
    return answer