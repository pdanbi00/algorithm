import sys
from datetime import datetime
input = sys.stdin.readline
N = int(input())
flower = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    flower.append((a*100+b, c*100+d))
flower.sort()

# 정원의 마지막 꽃이 지는 날짜
end_date = 301

# 심은 꽃의 개수
count = 0

while flower:
    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이후거나
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜랑 이어지지 않으면 종료
    if end_date>= 1201 or flower[0][0] > end_date:
        break
    # 꽃이 피는 날짜가 end_date 이전일 때, 가장 느리게 지는 꽃 날짜
    temp_end_date = -1

    for _ in range(len(flower)):
        # 꽃이 피는 날짜가 end_date 이전이라면 가능
        if flower[0][0] <= end_date:
            # 그 중에서 가장 느리게 지는 꽃의 날짜 확인
            if temp_end_date < flower[0][1]:
                temp_end_date = flower[0][1]
            # 확인한 꽃은 제거
            flower.remove(flower[0])
        else:
            break
    # 가장 꽃이 느리게 지는 날짜를 end_date로 수정
    end_date = temp_end_date
    # 심은 꽃 개수 추가
    count += 1

if end_date >= 1201:
    print(count)
else:
    print(0)