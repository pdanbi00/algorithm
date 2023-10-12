# 아이디어 : 0점부터 10점까지 중에 화살 맞는 중복조합을 다 구한다.
#           n이 3이면 10점 3개, 10점 1개, 9점 2개 이런식으로.
#           모든 경우를 돌면서 어피치 화살 갯수 추가함.
#           각 경우마다 점수 계산해서 제일 큰 값인경우를 찾는데 뒤로갈수록 갱신되도록
from itertools import combinations_with_replacement # 중복조합

def solution(n, info):
    answer = [-1]
    max_gap = -1
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 이렇게 해야 초반일수록 적은 숫자들이 포함 됨. 그래서 점수차 같은 경우는 굳이 고려 안해도 됨.
    combi = list(combinations_with_replacement(num, n))
    for com in combi:
        score = [0] * 11 # 라이언 점수. 이거도 앞쪽부터 10점, 9점 짜리
        for c in com: # 중복조합으로 뽑힌 조합의 하나의 수
            score[10-c] += 1 # 개수 카운팅
        a_score = 0
        l_score = 0
        for i in range(11):
            if info[i] == score[i] == 0: # 어피치랑 라이언 둘다 못 맞힌 경우
                continue
            elif info[i] >= score[i]: # 어피치가 더 많이 맞히거나 같게 맡힌 경우
                a_score += 10 - i
            else:
                l_score += 10 - i
        if l_score > a_score: # 라이언 점수가 어피치 점수보다 큰 경우
            gap = l_score - a_score
            if gap > max_gap:
                max_gap = gap
                answer = score

    return answer