def solution(s):
    answer = 0
    is_x, is_not_x = 0, 0 # x와 같은 글자 수, x와 다른 글자 수
    for i in range(len(s)):
        if is_x == is_not_x:
            answer += 1
            x = s[i]
            is_x, is_not_x = 0, 0
            
        if s[i] == x:
            is_x += 1
        else:
            is_not_x += 1
    return answer