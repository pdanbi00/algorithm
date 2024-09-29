N = int(input())
start = list(map(int, input()))
end = list(map(int, input()))

# 스위치를 누르는 순서는 상관이 없다.

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, N):
        if A_copy[i-1] == B[i-1]:
            continue
        press += 1
        for j in range(i-1, i+2):
            if j < N:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press
    else:
        return 1e9

result = change(start, end)
# 첫번째 스위치 켠 경우
start[0] = 1 - start[0]
start[1] = 1 - start[1]

result = min(result, change(start, end)+1)
if result == 1e9:
    print(-1)
else:
    print(result)