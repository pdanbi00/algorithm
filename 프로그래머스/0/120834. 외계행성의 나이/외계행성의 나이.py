def solution(age):
    answer = ''
    info = {0 : 'a', 1 : 'b', 2 : 'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    tmp = ''
    while age > 0:
        n = age % 10
        tmp += info[n]
        age //= 10
    for i in range(len(tmp)):
        answer += tmp[len(tmp)-1-i]
    return answer