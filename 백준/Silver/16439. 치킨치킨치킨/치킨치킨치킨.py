N, M = map(int, input().split())
prefers = []
for _ in range(N):
    prefer = list(map(int, input().split()))
    prefers.append(prefer)


chickens = [i for i in range(M)]
answer = 0
used = [False] * M

def func(idx, arr):
    global answer
    if len(arr) == 3:
        tmp = 0
        for i in range(N):
            m = 0
            for a in arr:
                m = max(m, prefers[i][a])
            tmp += m
        answer = max(answer, tmp)
        return

    for k in range(idx, M):
        if not used[k]:
            used[k] = True
            func(k, arr + [k])
            used[k] = False

func(0, [])
print(answer)