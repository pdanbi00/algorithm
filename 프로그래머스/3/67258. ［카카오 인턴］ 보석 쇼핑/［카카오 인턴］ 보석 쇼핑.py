def solution(gems):
    N = len(gems)
    kind = len(set(gems))
    dict = {gems[0] : 1}
    ans = [0, N-1]
    # 투포인터
    s, e = 0, 0
    while s < N and e < N:
        if len(dict) < kind: # 보석 종류가 부족할 경우
            e += 1
            if e == N:
                break
            dict[gems[e]] = dict.get(gems[e], 0) + 1
        else: # 보석 종류 다 포함되어 있으면 정답 구간이랑 비교
            if ans[1] - ans[0] + 1 > e - s + 1:
                ans = [s, e]
            if dict[gems[s]] == 1:
                del dict[gems[s]]
            else:
                dict[gems[s]] -= 1
            s += 1
    ans[0] += 1
    ans[1] += 1
    return ans