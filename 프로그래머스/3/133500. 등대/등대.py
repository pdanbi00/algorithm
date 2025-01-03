import sys
sys.setrecursionlimit(100001)
def dfs(node, graph, visited):
    visited[node] = True
    children = []
    for next_node in graph[node]:
        if not visited[next_node]:
            children.append(next_node)
            
    # 켰을 경우, 안켰을 경우를 리프노드부터 합산
    on, off = 1, 0
    
    # 리프 노드
    if len(children) == 0:
        return on, off
    else:
        for child in children:
            child_on, child_off = dfs(child, graph, visited)
            # 현재 노드가 켜져있다면 가장 작은 값 추가하기
            on += min(child_on, child_off)
            
            # 현재 노드가 꺼져 있다면 리프노드는 켜져있어야 됨
            off += child_on
        return on, off


def solution(n, lighthouse):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for a, b in lighthouse:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        
    answer = min(dfs(0, graph, visited))
    return answer