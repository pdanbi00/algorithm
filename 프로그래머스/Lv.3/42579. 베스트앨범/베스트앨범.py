def solution(genres, plays):
    answer = []
    dic = {}
    dic_count = {}
    length = len(genres)
    for i in range(length):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
            dic_count[genres[i]] = [(plays[i], i)]
        else:
            dic[genres[i]] += plays[i]
            dic_count[genres[i]].append((plays[i], i))
    for (k, value) in sorted(dic.items(), key=lambda x:x[1], reverse=True):
        for (gen, count) in sorted(dic_count[k], key=lambda x : x[0], reverse=True)[:2]:
            # print(gen, count)
            answer.append(count)
    
    return answer