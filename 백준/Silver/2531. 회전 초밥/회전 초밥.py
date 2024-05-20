# 3. 슬라이딩 윈도우
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
left = 0
right = 0

dict = {}
answer = 0
# k만큼 먹기
while right < k:
    if sushi[right] not in dict.keys():
        dict[sushi[right]] = 1
    else:
        dict[sushi[right]] += 1
    right += 1

if c not in dict.keys():
    dict[c] = 1
else:
    dict[c] += 1
    
# 슬라이딩 윈도우
while left < N:
    answer = max(answer, len(dict))
    # 1. 제일 왼쪽 초밥 제거
    dict[sushi[left]] -= 1
    # 삭제된 왼쪽 초밥이 0이면 dict에서 삭제
    if dict[sushi[left]] == 0:
        del dict[sushi[left]]
    # 위에서 k개 만큼 먹고 k가 1 증가한 상태라서 바로 right % N 하면 됨.
    if sushi[right % N] not in dict.keys():
        dict[sushi[right % N]] = 1
    else:
        dict[sushi[right % N]] += 1
    
    left += 1
    right += 1
# 처음에 k개 넣고 쿠폰에 해당하는 초밥도 추가 해서 더 만질거 없음.    
print(answer)  