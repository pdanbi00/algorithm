arr = list(input())
N =len(arr)
'''
(( : 뒷다리
)) : 앞다리

뒷다리 위치 < 앞다리 위치
'''

back = []
front = []
for i in range(N-1):
    if i < N-3:
        if arr[i] == arr[i+1] and arr[i] == '(':
            back.append(i)

    if arr[i] == arr[i + 1] and arr[i] == ')':
        front.append(i)

# print(back)
# print(front)
answer = 0
for i in range(len(back)):
    for j in range(len(front)):
        if back[i] <= front[j]:
            answer += len(front) - j
            break
print(answer)