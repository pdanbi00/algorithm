def solution(participant, completion):
    answer = ''
    dict = {}
    for c in completion:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    for p in participant:
        if p in dict:
            dict[p] -= 1
        else:
            answer = p
    for k, v in dict.items():
        if v < 0:
            answer = k
    return answer