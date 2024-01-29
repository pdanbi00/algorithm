# 이분 그래프인지 판단하는 방법 : 모든 정점의 양 끝이 다른 곳에 속해야 됨.
# 이분그래프가 아니라는건 예를 들어 5와 2가 연결되어 있는데 2를 이미 방문한 상태임.
# 즉, 2는 A 또는 B 중 하나가 이미 결정 된 상태. 5에서 2를 갈 수 있다면 5가 A인 상태라면 2가 B여야하는데 2도 이미 A니깐 이분그래프가 아님.

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [0] * (V+1) # 이분그래프를 A 또는 B로 색칠한다고 생각해보자. 이게 원래 checked역할 하는거임. 0이면 방문 안함. 1이면 A, 2이면 B란 뜻
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    def dfs(index, c): # return 값이 False면 이분그래프가 아님. True면 이분그래프가 맞음
        color[index] = c
        for next in graph[index]:
            if color[next] == 0:
                # 지금이 c 라면 연결되서 방문하는 곳은 3-c 이면 됨. 왜냐면 c가 1이면 방문하는데는 2가 되고 c가 2이면 방문하는데가 1이 됨
                if not dfs(next, 3-c): # 이분그래프가 아니라면 더이상 탐색할 필요가 없어서 return False
                    return False
            elif color[index] == color[next]: # 방문 해도 검사해야됨. 색이 정해진게 같으면 false
                return False
        return True
    ans = True
    for i in range(1, V+1):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
                break
    if ans == True:
        print('YES')
    else:
        print('NO')