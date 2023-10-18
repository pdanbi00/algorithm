# 아이디어 : 할인율은 10%, 20%, 30%, 40% 밖에 없다 그랬고 이모티콘은 최대 7개니깐 이모티콘의 모든 할인율 경우를 조합으로 꺼내서 계산

from itertools import product # 얘가 조합 만들어주는거

def solution(users, emoticons):
    emoticon_plus_user = 0
    emoticon_total = 0
    sale_type = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    for sale in sale_type: # 조합의 각 경우마다
        plus_user = 0
        sale_total = 0
        for user in users: 
            price = 0
            for i in range(len(emoticons)):
                if user[0] <= sale[i]: # 사용자가 사려는 할인율보다 크거나 같다면
                    price += emoticons[i] // 100 * (100 - sale[i])
            if price >= user[1]: # 이모티콘 샀을 때 금액 계산 했을때 플러스 기준 금액보다 크다면
                plus_user += 1 # 플러스 인원 추가
            else: # 플러스 기준 금액보다 작으면
                sale_total += price # 총 금액에 금액 추가
        if plus_user > emoticon_plus_user or plus_user == emoticon_plus_user and sale_total > emoticon_total: # 모든 이용자 다 계산 해봤을 때 기존까지의 플러스 인원보다 많거나 혹은 플러스 인원은 같지만 총 이모티콘 판매 금액이 더 크다면
            emoticon_plus_user = plus_user # 답 갱신
            emoticon_total = sale_total # 답 갱신
            
        
    
    answer = [emoticon_plus_user, emoticon_total]
    return answer