from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for perm in permutations(dungeons, len(dungeons)):
        cnt = 0
        blood = k
        for p in perm:
            if p[0] <= blood:
                blood -= p[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer