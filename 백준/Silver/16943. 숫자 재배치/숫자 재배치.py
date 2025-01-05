from itertools import permutations

A, B = input().split()
B = int(B)
arr = []
for perm in permutations(A, len(A)):
    tmp = ''.join(perm)
    if tmp[0] != '0':
        arr.append(int(tmp))

arr.sort()
ans = -1
for i in range(len(arr)):
    if arr[i] < B:
        ans = arr[i]
    else:
        break
print(ans)