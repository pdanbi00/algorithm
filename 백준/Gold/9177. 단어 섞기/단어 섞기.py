# BFS
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    word1, word2, word3 = input().split()
    idx = 0
    q = deque()
    q.append((0, 0)) # word1의 인덱스, word2의 인덱스
    visited = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            if a < len(word1) and visited[a+1][b] == 0 and word1[a] == word3[idx]:
                visited[a+1][b] = 1
                q.append((a+1, b))
            if b < len(word2) and visited[a][b+1] == 0 and word2[b] == word3[idx]:
                visited[a][b+1] = 1
                q.append((a, b+1))
        idx += 1
    if idx == len(word3) + 1:
        print(f'Data set {tc}: yes')
    else:
        print(f'Data set {tc}: no')