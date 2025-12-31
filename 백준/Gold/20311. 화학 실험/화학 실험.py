from heapq import heappush, heappop
N, K = map(int, input().split())
colors = list(map(int, input().split()))

q = []
for i in range(K):
    heappush(q, (-colors[i], i))

answer = []
possible = True
temp = []

while q:
    cnt, num = heappop(q)

    answer.append(num+1)
    if len(answer) >= 2 and answer[-1] == answer[-2]:
        possible = False
        break

    if temp:
        x = temp.pop()
        if x[0] < 0:
            heappush(q, x)


    temp.append((cnt+1, num)) # 개수를 내림차순으로 정렬하기 위해서 음수로 넣었으니깐 1씩 추가해서 없애주기

if not possible or temp[0][0] <= -1:
    print(-1)
else:
    print(*answer)