import bisect
T = int(input())
N = int(input())
A_arr = list(map(int, input().split()))
M = int(input())
B_arr = list(map(int, input().split()))

# 일정 구간 누적합 2개 더해서 T 되는지 확인하기
a = []
b = []
for i in range(N):
    total = 0
    for j in range(i, N):
        total += A_arr[j]
        a.append(total)

for i in range(M):
    total = 0
    for j in range(i, M):
        total += B_arr[j]
        b.append(total)

# B 배열에서만 찾으니깐 a는 정렬 안해도 됨
b.sort()

ans = 0

# bisect 라이브러리를 사용하면 리스트에 그 값이 존재하는지 index를 알 수 있음.

for i in range(len(a)):
    tmp = T - a[i]
    left = bisect.bisect_left(b, tmp) # 인덱스 반환
    right = bisect.bisect_right(b, tmp) # 인덱스 반환
    # tmp라는 값이 없으면 index가 배열길이 값으로 나올겅미.
    ans += (right - left)

print(ans)
