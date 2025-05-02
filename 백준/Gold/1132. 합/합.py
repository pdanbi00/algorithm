N = int(input())
alpha = [0] * 10 # 각 알파벳의 합산
zero = [True] * 10 # 0이 가능한 수
for _ in range(N):
    arr = list(input())
    n = len(arr)
    # 첫번째 수는 0이 될 수 없음
    zero[ord(arr[0])-65] = False
    for i in range(n):
        alpha[ord(arr[i])-65] += 10 ** (n-1-i)
new_alpha = []
for i, v in enumerate(alpha):
    new_alpha.append((i, v))
new_alpha.sort(key=lambda x : (-x[1], x[0]))

ans = 0
visited = [-1] * 10
cnt = 0 # 사용된 알파벳 개수 확인
for i in range(10):
    if alpha[i] > 0:
        cnt += 1

if cnt == 10:
    for i in range(len(new_alpha)-1, -1, -1):
        if new_alpha[i][1] > 0:
            if zero[new_alpha[i][0]] == True:
                new_alpha.pop(i)
                break
    for i in range(len(new_alpha)):
        ans += new_alpha[i][1] * (9-i)
else:
    for i in range(len(new_alpha)):
        ans += new_alpha[i][1] * (9-i)
print(ans)