arr = list(input())
N =len(arr)
'''
(( : 뒷다리
)) : 앞다리

뒷다리 위치 < 앞다리 위치
'''

answer = 0 # 순서쌍 개수
cnt = 0 # 뒷다리 개수

# 뒷다리 개수를 ) 찾은 개수만큼 더하면 됨
# ( 다음에 오는 )를 찾으면 그 전에 있던 ( 개수를 다 더하면 됨
for i in range(1, N):
    if arr[i] == arr[i-1]:
        if arr[i] == '(':
            cnt += 1
        else:
            answer += cnt

print(answer)