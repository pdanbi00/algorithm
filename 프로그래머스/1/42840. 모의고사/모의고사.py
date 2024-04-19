def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_1 = 0
    score_2 = 0
    score_3 = 0
    for i in range(len(answers)):
        if first[i%len(first)] == answers[i]:
            score_1 += 1
        if second[i%len(second)] == answers[i]:
            score_2 += 1
        if third[i%len(third)] == answers[i]:
            score_3 += 1
    ans = max(score_1, score_2, score_3)
    if score_1 == ans:
        answer.append(1)
    if score_2 == ans:
        answer.append(2)
    if score_3 == ans:
        answer.append(3)
    return answer