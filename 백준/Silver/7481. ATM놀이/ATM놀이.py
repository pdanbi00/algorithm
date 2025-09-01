T = int(input())
for _ in range(T):
    possible = False
    a, b, S = map(int, input().split())
    max_v = max(a, b)
    min_v = min(a, b)

    limit = S // max_v

    flag = [False] * min_v
    check = False
    for i in range(limit, -1, -1):
        remain = S - max_v * i
        mod = remain % min_v
        if flag[mod]:
            break

        flag[mod] = True
        if mod == 0:
            check = True
            answer = []
            if max_v == a:
                answer.append(i)
                answer.append(remain // min_v)
            else:
                answer.append(remain // min_v)
                answer.append(i)
            break
            
    if check:
        print(*answer)
    else:
        print("Impossible")