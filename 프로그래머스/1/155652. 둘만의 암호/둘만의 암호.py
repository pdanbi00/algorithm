def solution(s, skip, index):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for a in skip:
        alpha.remove(a)
    N = len(alpha)
    for a in s:
        tmp = (alpha.index(a) + index) % N
        answer += alpha[tmp]
    return answer