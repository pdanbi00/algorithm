def solution(s):
    answer = True
    N = len(s)
    p = 0
    y = 0
    for i in range(N):
        if s[i] == 'P' or s[i] == 'p':
            p += 1
        elif s[i] == 'Y' or s[i] == 'y':
            y += 1
    if p == y:
        return True
    else:
        return False