def solution(genres, plays):
    answer = []
    total = {} # {장르 : 총 재생 횟수}
    genre = {} # {장르 : [(플레이 횟수, 고유번호)]}
    
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]
            
        if genres[i] in genre:
            genre[genres[i]] += [(plays[i], i)]
        else:
            genre[genres[i]] = [(plays[i], i)]
            
    # 재생 횟수 내림차순으로 장르 정렬
    sorted_genre = sorted(total.items(), key=lambda x : x[1], reverse = True)
    # 재생 횟수 기준 내림차순, 인덱스 기준 오름차순
    for gen, totalPlay in sorted_genre:
        genre[gen] = sorted(genre[gen], key=lambda x: (-x[0], x[1]))
        answer += [idx for play, idx in genre[gen][:2]]
    return answer