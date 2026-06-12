def solution(num_list, n):
    answer = []
    N = len(num_list)
    idx = 0
    while idx < N:
        tmp = []
        for i in range(n):
            tmp.append(num_list[idx])
            idx += 1
        answer.append(tmp)
    return answer