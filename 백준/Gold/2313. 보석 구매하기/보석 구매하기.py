import sys
input = sys.stdin.readline

N = int(input())
total = 0
result = ''
for _ in range(N):
    L = int(input())
    jewerly = list(map(int, input().split()))

    mx = jewerly[0]
    mx_start = mx_end = 0

    start = 0
    end = 0

    for i in range(1, L):
        if jewerly[i] >= jewerly[i-1] + jewerly[i]:
            start = i
            end = i
        else:
            jewerly[i] = jewerly[i-1] + jewerly[i]
            end = i

        if jewerly[i] > mx:
            mx = jewerly[i]
            mx_start = start
            mx_end = end
        elif jewerly[i] == mx and mx_end - mx_start > end - start:
            mx = jewerly[i]
            mx_start = start
            mx_end = end

    total += mx
    result += f'{mx_start+1} {mx_end+1}\n'

print(total)
print(result)