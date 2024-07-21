from collections import deque
N = int(input())
fruits = list(map(int, input().split()))

ans = 0
start = 0
end = 0

next_start = 0

kind = []

while start <= end and end < N:
    if len(kind) < 2:
        if fruits[end] not in kind:
            kind.append(fruits[end])
    else:
        if fruits[end] not in kind:
            ans = max(ans, end-start)

            # next_start 있는 과일이랑 다른 종류의 과일 kind에서 제거
            for i in range(len(kind)):
                if kind[i] != fruits[next_start]:
                    kind.pop(i)
                    break

            kind.append(fruits[end])
            start = next_start
    if fruits[end-1] != fruits[end]:
        next_start = end
    end += 1

ans = max(ans, N-start)
print(ans)