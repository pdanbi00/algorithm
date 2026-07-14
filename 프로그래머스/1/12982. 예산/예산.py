def solution(d, budget):
    answer = 0
    d.sort()
    every = True
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            answer = i
            every = False
            break
    if every:
        answer = len(d)
    return answer