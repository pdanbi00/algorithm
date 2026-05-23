def solution(dirs):
    answer = 0
    info = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    r, c = 0, 0
    visited = set()
    for d in dirs:
        if -5 <= r + info[d][0] <= 5 and -5 <= c + info[d][1] <= 5:
            dr = r + info[d][0]
            dc = c + info[d][1]
            
            if (r, c, dr, dc) not in visited and (dr, dc, r, c) not in visited:
                print(r, c, dr, dc)
                answer += 1
                visited.add((r, c, dr, dc))
            
            r = dr
            c = dc
            
        else:
            continue
            
    return answer