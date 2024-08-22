# 최소면 BFS 같은데...
# 풀이 자체를 모르겠네
# DFS를 돌면서 결과값을 갱신하는 수 밖에? 아니었다~~

# visited로 방문체크도 못할거같은디... 맞음...
# 이것은 놀랍게도 이차원 배열로 생각하는게 아니라 123456780 문자열로 생각해야 됨.

from collections import deque

# 퍼즐을 문자열 123456780으로 정렬시킨다고 생각
puzzle = ""
for _ in range(3):
    puzzle += "".join(list(input().split()))

visited = {} # 문자열을 키 값으로 해서 움직인 횟수를 value로 저장해서 방문확인
q = deque() # 수를 이동시킨 결과 문자열 담음

visited[puzzle] = 0
q.append(puzzle)

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while q:
        puzzle = q.popleft()
        cnt = visited[puzzle]
        z = puzzle.index('0') # 0(빈칸) 위치

        if puzzle == '123456780':
            return cnt

        r = z // 3 # 2차원 배열로 변환시 행
        c = z % 3 # 2차원 배열로 변환시  열

        cnt += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc # 문자열에서의 위치로 인덱스 변환
                puzzle_list = list(puzzle) # 원소 스와핑을 위해서 문자열을 리스트로 변환
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
                new_puzzle = "".join(puzzle_list) # 딕셔너리에 넣기 위해서 다시 문자열로 변환

                # 방문 안 한 문자열이라면
                if new_puzzle not in visited:
                    visited[new_puzzle] = cnt
                    q.append(new_puzzle)

    return -1

print(bfs())