def solution(my_string):
    answer = 0
    idx = 0
    num = ""
    N = len(my_string)
    
    while (idx < N):
        c = my_string[idx]
        if (not c.isnumeric()):
            if (num != ""):
                answer += int(num)
                num = ""
            idx += 1
            continue
        else:
            num += c
            idx += 1
    if num != "":
        answer += int(num)
    return answer