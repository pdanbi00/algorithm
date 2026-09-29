resultCount = 0
resultPrice = 0
discount = []
def solution(users, emoticons):
    answer = [] 
    global discount
    discount = [0] * len(emoticons)
    
    func(0, users, emoticons)
    answer.append(resultCount)
    answer.append(resultPrice)
    return answer

def func(idx, users, emoticons):
    global resultCount, resultPrice, discount
    
    if idx == len(emoticons):
        totalCount = 0
        totalPrice = 0
        for i in range(len(users)):
            minPercent = users[i][0]
            minPrice = users[i][1]
            
            total = 0
            for j in range(len(emoticons)):
                if minPercent <= discount[j]:
                    total += emoticons[j] * (100 - discount[j]) // 100  

            if total >= minPrice:
                totalCount += 1
            else:
                totalPrice += total

        if resultCount < totalCount:
            resultCount = totalCount
            resultPrice = totalPrice
        elif resultCount == totalCount and resultPrice < totalPrice:
            resultPrice = totalPrice
            
    else:
        for k in range(10, 41, 10):
            discount[idx] = k
            func(idx+1, users, emoticons)
            
            
            
            
            