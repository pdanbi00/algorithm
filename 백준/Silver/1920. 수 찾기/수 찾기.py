N = int(input())
N_num = list(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))
N_num.sort()

# 시간 초과 걸리기 때문에 이분탐색
for num in M_num:
    start, finish = 0, N-1
    isExist = False # 찾았는지 여부

    while start <= finish:
        mid = (start + finish) // 2
        if num == N_num[mid]: # 목표값이 존재한다면
            isExist = True
            print(1)
            break
        elif num > N_num[mid]:
            start = mid + 1
        else:
            finish = mid - 1
    if isExist == False:
        print(0)
            