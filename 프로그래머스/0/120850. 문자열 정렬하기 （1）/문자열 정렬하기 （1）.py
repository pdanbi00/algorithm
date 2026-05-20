def solution(my_string):
    answer = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    N = len(my_string)
    for i in range(N):
        if my_string[i] in num:
            answer.append(int(my_string[i]))
    answer.sort()
    return answer