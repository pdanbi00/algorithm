def solution(k, m, score):
    
    answer = 0
    score.sort(reverse=True)
    num = (len(score)//m) * m
    
    arr=[]
    for i in range(1,num+1):
        arr.append(score[i-1])
        if i%m == 0:
            answer+=min(arr)*m
            arr=[]
            
    return answer