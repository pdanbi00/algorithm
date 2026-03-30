N = int(input())
nums = list(map(int, input().split()))

even = 0
odd = 0
for i in range(N):
    if i % 2 == 0:
        odd += nums[i]
    else:
        even += nums[i]

if odd == even:
    print(0)
else:
    possible = True
    if N == 3:
        if odd > even:
            possible = False

    if not possible:
        print(-1)
    else:
        print(abs(odd - even))