T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    arr = [[0] * n for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j] = j+1
            else:
                if j == 0:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]
    print(arr[k][n-1])