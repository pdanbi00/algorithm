N, K, P, X = map(int, input().split())

# 자릿수 맞춰주기
if len(str(X)) < K:
    cx = '0' * (K-len(str(X))) + str(X)
else:
    cx = str(X)

# 0부터 9까지 디스플레이에 보이는대로 표시
num = ['1110111', '0010010', '1011101', '1011011', '0111010', '1101011', '1101111', '1010010', '1111111', '1111011']

# arr[i][j] : i가 j가 되기 위해서 반전시켜야하는 개수
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            d = 0
            for k in range(7):
                if num[i][k] != num[j][k]:
                    d += 1
            arr[i].append(d)
ans = 0
for i in range(1, N+1): # 반전해서 1이상 N이하가 되도록
    if int(i) != int(cx):
        # 자릿수 맞춰주기
        if len(str(i)) < K:
            cy = '0' * (K - len(str(i))) + str(i)
        else:
            cy = str(i)
        tmp = 0
        for j in range(K):
            tmp += arr[int(cx[j])][int(cy[j])]
            if tmp > P:
                break
        else:
            ans += 1
print(ans)