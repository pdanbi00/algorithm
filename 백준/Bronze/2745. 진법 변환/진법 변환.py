num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
answer = 0
B = int(B)
for i, num in enumerate(N[::-1]):
    answer += B ** i * num_list.index(num)

print(answer)