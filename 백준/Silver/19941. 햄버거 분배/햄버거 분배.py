N, K = map(int, input().split())
info = list(input())

answer = 0
visited = [0] * N
idx = 0
while idx < N:
    if info[idx] == 'P':
        visited[idx] = 1
        for i in range(-K, K+1):
            if 0 <= idx + i < N:
                if visited[idx + i] == 0 and info[idx+i] == 'H':
                    visited[idx+i] = 1
                    answer += 1
                    break
    idx += 1
print(answer)