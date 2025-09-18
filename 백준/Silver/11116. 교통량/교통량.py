T = int(input())
for _ in range(T):
    m = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    total = []
    for i in range(m):
        total.append(left[i])
        total.append(right[i])

    total.sort()
    cnt = 0
    while total:
        tmp1 = total[0]
        tmp2 = total[0] + 500
        tmp3 = total[0] + 1000
        tmp4 = total[0] + 1500

        if tmp1 in left and tmp2 in left and tmp3 in right and tmp4 in right:
            cnt += 1
            total.remove(tmp1)
            total.remove(tmp2)
            total.remove(tmp3)
            total.remove(tmp4)
        elif tmp1 in right and tmp2 in right and tmp3 in left and tmp4 in left:
            total.remove(tmp1)
            total.remove(tmp2)
            total.remove(tmp3)
            total.remove(tmp4)
    print(cnt)