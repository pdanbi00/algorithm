A = input()
B = input()
N = len(A)

cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
tmp = []
for i in range(N):
    tmp.append(cnt[ord(A[i])-65])
    tmp.append(cnt[ord(B[i])-65])

while len(tmp) > 2:
    arr = []
    for i in range(len(tmp)-1):
        arr.append((tmp[i] + tmp[i+1]) % 10)
    tmp = arr

print(str(arr[0]) + str(arr[1]))