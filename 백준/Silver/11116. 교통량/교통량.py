T = int(input())
for _ in range(T):
    m = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))


    cnt = 0
    while left:
        tmp = left[0]

        if tmp in left and tmp+500 in left and tmp+1000 in right and tmp+1500 in right:
            cnt += 1
        left.pop(0)
    print(cnt)