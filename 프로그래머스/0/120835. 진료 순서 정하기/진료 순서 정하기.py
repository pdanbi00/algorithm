def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    N = len(emergency)
    for i in range(N):
        answer.append(sorted_emergency.index(emergency[i])+1)
    return answer