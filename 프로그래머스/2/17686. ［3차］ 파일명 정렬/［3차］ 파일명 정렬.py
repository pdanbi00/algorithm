def solution(files):
    answer = []
    N = len(files)
    new_file = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for idx in range(N):
        tmp = [files[idx]]
        find_num1 = -1
        find_num2 = -1
        head = []
        number = ''
        for i in range(len(files[idx])):
            if files[idx][i] in num and find_num1 == -1:
                find_num1 = i
                find_num2 = i
            elif find_num1 == -1 and files[idx][i] not in num:
                head.append(files[idx][i].upper())    
            elif find_num1 != -1 and files[idx][i] not in num:
                find_num2 = i
                break
        for i in range(find_num1, find_num2):
            number += files[idx][i]
        number = int(number)
        tmp.append(head)
        tmp.append(number)  
        tmp.append(idx)
        new_file.append(tmp)
        
    new_file.sort(key=lambda x : (x[1], x[2], x[3]))
    for i in range(N):
        answer.append(new_file[i][0])
            
    return answer