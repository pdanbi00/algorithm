# 아이디어 : query에서 나올 수 있는 모든 경우를 딕셔너리로 만듦.(점수 제외)
#          그리고 info를 돌면서 앞서 만든 딕셔너리에 key 값이랑 같은 것들에 점수를 추가
#          query와 일치하는 딕셔너리에서 점수들을 이분 탐색으로 세서 갯수 파악

def solution(info, query):
    dic = {}
    
    # 나올 수 있는 모든 조건 딕셔너리로 만들기
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    dic[(a, b, c, d)] = []
    
    # info에서 딕셔너리 키와 일치하는 것들 값 value로 넣어주기
    for inf in info:
        i = inf.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        dic[(a, b, c, d)].append(int(i[4])
                        
    
    # 이제 이분탐색할거임. 그러기 위해서 정렬하셈
    for k in dic.keys():
        dic[k].sort()
                                                 
    answer = []
        
    for qu in query:
        q = qu.split()
        scores = dic[(q[0], q[2], q[4], q[6])]
        want = int(q[7])
        l, r = 0, len(scores)
        while l < r:
            middle = (l + r) // 2
            if scores[middle] >= want:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores) - l)
    
    return answer