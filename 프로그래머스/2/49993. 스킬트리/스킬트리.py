def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        idx = 0
        possible = True
        for i in range(len(s)):
            if s[i] in skill:
                if skill[idx] == s[i]:
                    idx += 1
                    continue
                else:
                    possible = False
        if possible:
            answer += 1
    return answer