N = int(input())
water = list(map(int, input().split()))

# 이진탐색
# 용액의 i번째 값과 i + 1부터 n까지의 값의 합을 이진탐색으로 구해서 0이랑 가장 가까운 쌍을 찾음
ans = abs(water[0] + water[N-1])
ans_left = 0
ans_right = N-1

for i in range(N-1):
    current = water[i]
    start = i+1
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + water[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1
print(water[ans_left], water[ans_right])