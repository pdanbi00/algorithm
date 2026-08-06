def solution(s):
    tmp = list(s)
    tmp.sort(reverse=True)
    answer = ''.join(tmp)
    return answer