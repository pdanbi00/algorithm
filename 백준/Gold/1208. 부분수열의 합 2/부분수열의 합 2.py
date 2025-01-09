# 이분 탐색

# 1. 수열을 반으로 나눔
# 2. 왼쪽 반에서 가능한 모든 부분집합의 합을 배열 A에 저장.
#    오른쪽 반에서 가능한 모든 부분집합의 합을 배열 B에 저장
# 3. A배열 중 하나, B배열 중 하나를 골라서 더해서 S가 되는 것 찾기

from itertools import combinations
from bisect import bisect_left, bisect_right

## bisect_left : 찾고자하는 값이 처음 등장하는 인덱스
## bisect_Right : 찾고자하는 값보다 큰 수 중 가장 작은 수의 인덱스 반환
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = nums[:N//2]
right = nums[N//2:]
left_sum = []
right_sum = []

# 왼쪽 반에서 가능한 모든 부분 집합 찾고 합 더하기
for i in range(1, len(left)+1):
    for combi in combinations(left, i):
        left_sum.append(sum(combi))
left_sum.sort()

# 오른쪽 반에서 가능한 모든 부분 집합 찾고 합 더하기
for i in range(1, len(right)+1):
    for combi in combinations(right, i):
        right_sum.append(sum(combi))
right_sum.sort()

ans = 0

# 왼쪽 수열 부분집합 합 중에 S인 값 확인하기
ans += bisect_right(left_sum, S) - bisect_left(left_sum, S)

# 오른쪽 수열 부분집합 합 중에 S인 값 확인하기
ans += bisect_right(right_sum, S) - bisect_left(right_sum, S)

# 왼쪾 수열 부분집합 합과 오른쪽 수열 부분집합 합이 S인 값 확인하기
for l in left_sum:
    find = S - l
    ans += bisect_right(right_sum, find) - bisect_left(right_sum, find)

print(ans)