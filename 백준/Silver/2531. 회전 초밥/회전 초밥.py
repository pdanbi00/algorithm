# 브루트포스
# 그냥 초밥 k개씩 잘라서 종류 개수 세고, 쿠폰에 있는 초밥은 그냥 무조건 공짜로 먹을 수 있으니깐 그거 추가해서 종류 개수 세기
import sys
input = sys.stdin.readline

sushi = []
N, d, k, c = map(int, input().split())
for i in range(N):
    n = int(input())
    sushi.append(n)
max_type = 0
for i in range(N):
    if i + k > N:
        number_type = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
    else:
        number_type = len(set(sushi[i:(i+k)] + [c]))
    max_type = max(max_type, number_type)
print(max_type)