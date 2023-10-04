# 아이디어 : 할인율은 10%, 20%, 30%, 40% 밖에 없다 그랬고 이모티콘은 최대 7개니깐 이모티콘의 모든 할인율 경우를 조합으로 꺼내서 계산

from itertools import product # 얘가 조합 만들어주는거

def solution(users, emoticons):
    emoticon_plus_user = 0
    emoticon_total = 0
    sale_type = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    for sale in sale_type:
        plus_user = 0
        sale_total = 0
        for user in users:
            price = 0
            for i in range(len(emoticons)):
                if user[0] <= sale[i]:
                    price += emoticons[i] // 100 * (100 - sale[i])
            if price >= user[1]:
                plus_user += 1
            else:
                sale_total += price
        if plus_user > emoticon_plus_user or plus_user == emoticon_plus_user and sale_total > emoticon_total:
            emoticon_plus_user = plus_user
            emoticon_total = sale_total
            
        
    
    answer = [emoticon_plus_user, emoticon_total]
    return answer