K, N = map(int, input().split())
length = []
for _ in range(K):
    length.append(int(input()))
start = 1
end = max(length)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(K):
        count += length[i]//mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)







# length.sort(reverse=True)
# l = (sum(length) // N)
# count = 0
# if K == N:
#     print(min(length))
# else:
#     while count < N:
#         count = 0
#         if (length[0] // l) * K >= N:
#             for i in range(K):
#                 count += length[i] // l
#                 if count >= N:
#                     break
#             if count >= N:
#                 break
#             l -= 1
#         else:
#             l -= 1
#     print(l)