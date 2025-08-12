max_v = -1
r = 0
c = 0

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] > max_v:
            max_v = arr[j]
            r = i+1
            c = j+1

print(max_v)
print(r, c)