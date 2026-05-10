def solution(my_string):
    answer = 0
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in my_string:
        if a in num:
            answer += int(a)
    return answer