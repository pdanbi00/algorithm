def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] == -1:
            if s >= 0:
                return False
        elif sign[i][index] == 1:
            if s <= 0:
                return False
    return True

def func(index):
    if index == N:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and func(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index] # 이러면 sign[index][index] 부호에 따라서 1부터 10 혹은 -1부터 -10까지 됨.
        if check(index) and func(index+1):
            return True
    return False

N = int(input())
line = input()
sign = [[0]*N for _ in range(N)]
ans = [0] * N
cnt = 0

# line에 적혀있는 부호들 매트릭스에 넣어주기
for i in range(N):
    for j in range(i, N):
        if line[cnt] == '0':
            sign[i][j] = 0
        elif line[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

func(0)
print(' '.join(map(str, ans)))
