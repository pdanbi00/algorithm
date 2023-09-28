# 아이디어 : 맨해튼 거리 2 초과여야하니깐
# 맨해튼 거리 1이면 바로 옆에 있는거니깐 거리두기 안된거
# 맨해튼 거리 2이면 파티션 확인

def solution(places):
    answer = []
    for place in places:
        answer.append(checkpartition(place))
    return answer

def checkpartition(place):
    people = []
    # 사람들 위치 확인
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append([i, j])
                
    for i in range(len(people)):
        r1, c1 = people[i]
        for j in range(i+1, len(people)):
            r2, c2 = people[j]
            distance = abs(r1 - r2) + abs(c1 - c2)
            
            if distance == 1: # 바로 옆에 있는 상황
                return 0
            elif distance == 2:
                if r1 == r2: # 같은 행에 있으면 중간 열에 파티션 없으면 거리두기 X
                    if place[r1][c1 + 1] == 'O':
                        return 0
                elif c1 == c2: # 같은 열에 있으면 중간 행에 파티션 없으면 거리두기ㅣ X
                    if place[r1 + 1][c1] == 'O':
                        return 0
                else: # 대각선에 있는 상황
                    if c1 < c2:
                        if not(place[r1][c2] == 'X' and place[r2][c1] == 'X'):
                            return 0
                    else:
                        if not(place[r1][c2] == 'X' and place[r2][c1] == 'X'):
                            return 0
    return 1
                