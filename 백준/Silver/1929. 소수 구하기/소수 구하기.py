M, N = map(int, input().split())
# for i in range(M, N+1):
#     for j in range(2, i-1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
# arr = list(range(M, N+1))
# for i in range(2, N):
#     for j in range(N-M + 1):
#         if arr[j] != i and arr[j] % i == 0:
#             arr[j] = 0
#         if arr[j] == i:
#             print(arr[j])
for i in range(M, N+1):
    is_prime = True
    if i == 1:
        continue
    for j in range(2, int(i**(0.5)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        print(i)

