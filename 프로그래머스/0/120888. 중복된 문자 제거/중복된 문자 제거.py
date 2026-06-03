def solution(my_string):
    answer = ''
    used = set()
    for i in range(len(my_string)):
        if my_string[i] in used:
            continue
        answer += my_string[i]
        used.add(my_string[i])
    return answer