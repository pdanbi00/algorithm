from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    
    q = deque()
    for city in cities:
        city = city.lower()
        # city가 q에 포함되어 있는 경우
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        # city가 q에 포함되어 있지 않은 경우
        else:
            # 캐시가 다 찬 경우
            if len(q) == cacheSize:
                q.popleft()
                q.append(city)
                answer += 5
            else:
                q.append(city)
                answer += 5
        
    return answer