def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
            
        if 65 <= ord(s[i]) <= 90:
            tmp = ord(s[i]) + n
            if tmp > 90:
                tmp -= 90
                tmp += 64
        elif 97 <= ord(s[i]) <= 122:
            tmp = ord(s[i]) + n
            if tmp > 122:
                tmp -= 122
                tmp += 96
        answer += chr(tmp)
    return answer

'''
A 65
Z 90
a 97
z 122
'''