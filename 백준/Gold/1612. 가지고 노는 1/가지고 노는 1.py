N = int(input())
temp = 1
ans = 1

if N % 2 == 0 or N % 5 == 0:
    print(-1)
    exit()

while temp % N != 0:
    temp = (temp % N) * 10 + 1
    # print(temp)
    ans += 1

print(ans)