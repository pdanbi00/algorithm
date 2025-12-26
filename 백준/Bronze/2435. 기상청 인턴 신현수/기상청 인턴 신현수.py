N, K = map(int, input().split())
temp = list(map(int, input().split()))
total_temp = [0] * N
total_temp[0] = temp[0]
for i in range(1, N):
    total_temp[i] = total_temp[i-1] + temp[i]

answer = total_temp[K-1]
for i in range(K, N):
    answer = max(answer, total_temp[i] - total_temp[i-K])

print(answer)