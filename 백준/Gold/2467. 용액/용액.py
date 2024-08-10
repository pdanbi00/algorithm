N = int(input())
water = list(map(int, input().split()))

# 투포인터
start = 0
end = N-1

min_ans = abs(water[0] + water[N-1]) # abs(tmp)로 업데이트 할거야
ans = [water[start], water[end]]
while start < end: # 왼쪽 값이랑 오른쪽 값이 같을 수는 없음
    tmp = water[start] + water[end]
    if abs(tmp) < min_ans:
        min_ans = abs(tmp)
        ans = [water[start], water[end]]
        if min_ans == 0:
            break
    if tmp < 0: # 0보다 작으면 값을 키워야하기 때문에 왼쪽 포인터 증가시키기
        start += 1
    else:
        end -= 1

print(*ans)