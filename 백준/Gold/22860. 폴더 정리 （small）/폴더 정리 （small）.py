from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info = dict()

def find_files(start):
    global cnt
    q = deque([start])
    while q:
        cur = q.popleft()
        for p in info[cur]:
            if p in info:
                q.append(p)
            else: # 파일인 경우
                files.add(p)
                cnt += 1

for _ in range(N+M):
    P, F, C = input().rstrip().split()
    if P not in info:
        info[P] = []
    if C == '1' and F not in info:
        info[F] = []

    info[P].append(F)

Q = int(input())
for _ in range(Q):
    files = set()
    cnt = 0
    path = list(map(str, input().rstrip().split('/')))
    find_files(path[-1])
    print(len(files), cnt)