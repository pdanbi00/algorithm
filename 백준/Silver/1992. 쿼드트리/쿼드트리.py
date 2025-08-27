def compression(arr):
    if len(arr) == 1:
        return str(arr[0][0])

    l = len(arr)
    # 모두 같다면 그 값만 보내기
    num = arr[0][0]
    possible = True
    for i in range(l):
        for j in range(l):
            if arr[i][j] != num:
                possible = False
                break
        if not possible:
            break

    if possible:
        return str(num)

    result = ''

    for k in [0, l//2]:
        for p in [0, l//2]:
            tmp = [[0] * (l//2) for _ in range(l//2)]
            for i in range(l//2):
                for j in range(l//2):
                    tmp[i][j] = arr[k+i][p+j]
            result += compression(tmp)
    return '(' + result + ')'

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
print(compression(board))