# 슬라이딩 윈도우
arr = list(input())
n = len(arr)
cnt = arr.count('a')

ans = 1e9

# 원형 문자열이라고 했기 때문에 쉽게 계산하기 위해서 문자열 이어붙이기
arr += arr[0:cnt-1]
# a가 다 이어져야하니깐 0부터 a개수만큼 잘라서 b 개수 확인하기

for i in range(n):
    ans = min(ans, arr[i:i+cnt].count('b'))
print(ans)