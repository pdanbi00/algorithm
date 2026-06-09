def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    N = len(emergency)
    for i in range(N):
        for j in range(1, N+1):
            if emergency[i] == sorted_emergency[j-1]:
                answer.append(j)
    return answer