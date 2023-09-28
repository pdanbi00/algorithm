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
            
            if distance == 1:
                return 0
            elif distance == 2:
                if r1 == r2:
                    if place[r1][c1 + 1] == 'O':
                        return 0
                elif c1 == c2:
                    if place[r1 + 1][c1] == 'O':
                        return 0
                else:
                    if c1 < c2:
                        if not(place[r1][c2] == 'X' and place[r2][c1] == 'X'):
                            return 0
                    else:
                        if not(place[r1][c2] == 'X' and place[r2][c1] == 'X'):
                            return 0
    return 1
                