from collections import deque

T = int(input())
for _ in range(T):
    possible = False
    c1, r1, c2, r2 = input().split()
    c1 = ord(c1) - 65
    c2 = ord(c2) - 65
    r1 = 8 - int(r1)
    r2 = 8 - int(r2)

    q = deque()
    visited = set() # (1, r, c) , (3, r, c) (몇번째 이동인지, 행, 열)

    q.append([(r1, c1)])
    visited.add((0, r1, c1))
    ans = 'Impossible'
    while q:
        history = q.popleft()
        cnt = len(history)
        # print(history[-1])
        r = history[-1][0]
        c = history[-1][1]
        if len(history) >= 4:
            continue

        if history[-1][0] == r2 and history[-1][1] == c2:
            ans = history
            break

        # 오른쪽 위 대각선 확인
        nr, nc = r, c
        while True:
            nr -= 1
            nc += 1
            if 0 <= nr < 8 and 0 <= nc < 8:
                if (cnt+1, nr, nc) not in visited:
                    q.append(history + [(nr, nc)])
                    visited.add((cnt+1, nr, nc))
            else:
                break

        # 오른쪽 아래 대각선 확인
        nr, nc = r, c
        while True:
            nr += 1
            nc += 1
            if 0 <= nr < 8 and 0 <= nc < 8:
                if (cnt + 1, nr, nc) not in visited:
                    q.append((history + [(nr, nc)]))
                    visited.add((cnt + 1, nr, nc))
            else:
                break

        # 왼쪽 위 대각선 확인
        nr, nc = r, c
        while True:
            nr -= 1
            nc -= 1
            if 0 <= nr < 8 and 0 <= nc < 8:
                if (cnt + 1, nr, nc) not in visited:
                    q.append((history + [(nr, nc)]))
                    visited.add((cnt + 1, nr, nc))
            else:
                break

        # 왼쪽 아래 대각선 확인
        nr, nc = r, c
        while True:
            nr += 1
            nc -= 1
            if 0 <= nr < 8 and 0 <= nc < 8:
                if (cnt + 1, nr, nc) not in visited:
                    q.append((history + [(nr, nc)]))
                    visited.add((cnt + 1, nr, nc))
            else:
                break


    if ans == 'Impossible':
        print(ans)
    else:
        print(len(ans)-1, end=" ")
        for r, c in ans:
            print(chr(c + 65), 8-r, end=" ")


    '''
    q = (r1, c1, [(r1, c1), (r2, c2), (r3, c4)], ...
    
    제일 마지막 위치를 pop(). 근데 pop한 요소의 총 길이가 4면 더이상 움직일 수 없음.
    대각선 오른쪽 위, 대각선 왼쪽 위, 대각선 오른쪽 아래, 대각선 왼쪽 아래
    이렇게 크게 4 방향을 봐야 함.
    근데 대각선으로 한칸만 움직인 경우, 두칸만 움직인 경우 다 다르게 처리해야 됨.
    해당 칸을 방문 했는지는 visited를 통해서 확인. 근데 몇번째 이동으로 해당 칸에 왔는지도 보긴 해야 할 듯
    '''
