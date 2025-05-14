S = list(input())
cnt_arr = [[0] * 26 for _ in range(len(S))]
for i in range(len(S)):
    cnt_arr[i][ord(S[i])-97] += 1

for i in range(1, len(S)):
    for j in range(26):
        cnt_arr[i][j] += cnt_arr[i-1][j]
q = int(input())
for _ in range(q):
    arr = list(input().split())
    target, s, e = arr[0], int(arr[1]), int(arr[2])
    if s == 0:
        print(cnt_arr[e][ord(target)-97])
    else:
        print(cnt_arr[e][ord(target)-97] - cnt_arr[s-1][ord(target)-97])