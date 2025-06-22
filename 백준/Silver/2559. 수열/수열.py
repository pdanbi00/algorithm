N, K = map(int, input().split())
temperature = list(map(int, input().split()))
sum_arr = [0] * N
sum_arr[0] = temperature[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1] + temperature[i]
# print(sum_arr)
ans = sum_arr[K-1]
for i in range(K, N):
    tmp = sum_arr[i] - sum_arr[i-K]
    # print(i, i-K, tmp)
    ans = max(ans, tmp)
print(ans)