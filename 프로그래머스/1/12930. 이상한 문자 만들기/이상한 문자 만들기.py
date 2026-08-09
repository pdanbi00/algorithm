def solution(s):
    answer = ''
    line = s.split(" ")
    for word in line:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    return answer[:-1]