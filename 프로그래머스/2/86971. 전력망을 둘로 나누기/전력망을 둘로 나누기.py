from collections import deque

def solution(n, wires):
    answer = n
    for i in range(n-1):
        wire_arr = []
        graph = [[] for _ in range(n+1)]
        for j in range(n-1):
            if i != j:
                graph[wires[j][0]].append(wires[j][1])
                graph[wires[j][1]].append(wires[j][0])
        visited = [0] * (n+1)
        for j in range(1, n+1):
            if visited[j] == 0:
                q = deque()
                q.append(j)
                visited[j] = 1
                cnt = 1
                while q:
                    now = q.popleft()
                    for next in graph[now]:
                        if visited[next] == 0:
                            q.append(next)
                            visited[next] = 1
                            cnt += 1
                wire_arr.append(cnt)
        answer = min(answer, abs(wire_arr[0] - wire_arr[1]))
    return answer