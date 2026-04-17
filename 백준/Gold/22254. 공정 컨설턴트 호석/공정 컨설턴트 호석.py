from heapq import heappush, heappop
N, X = map(int, input().split())
task = list(map(int, input().split()))
s, e = 0, N
answer = 10 ** 15

if N == 1:
    print(1)
else:
    while s <= e:
        mid = (s+e) // 2

        q = []
        for i in range(mid):
            heappush(q, (task[i]))

        time = 0
        idx = mid
        while q:
            t = heappop(q)
            time = t
            if idx < N:
                heappush(q, (task[idx] + time))
                idx += 1

        if mid != 0 and time <= X:
            answer = min(answer, mid)
            e = mid - 1
        else:
            s = mid + 1
    if answer == 0:
        answer += 1
    print(answer)