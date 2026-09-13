def solution(my_str, n):
    answer = []
    N = len(my_str)
    idx = 0
    while idx < N:
        tmp = ''
        for _ in range(n):
            if idx < N:
                tmp += my_str[idx]
                idx += 1
        answer.append(tmp)
    return answer