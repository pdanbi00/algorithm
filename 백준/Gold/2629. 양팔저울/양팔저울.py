# N = int(input())
# dp[i][j] : i개의 추를 사용해서 j라는 무게를 만듦
# 즉, dp[사용한 추의 개수][양쪽 저울의 추 무게의 차이]

chu_cnt = int(input())
chu_list = list(map(int, input().split()))
bead_cnt = int(input())
bead_list = list(map(int, input().split()))

def cal(cnt, weight):
    if (cnt > chu_cnt):
        return
    if (dp[cnt][weight]):
        return

    dp[cnt][weight] = True
    # 1. 추를 저울의 오른쪽에 올리는 경우
    cal(cnt + 1, weight + chu_list[cnt-1])
    # 2. 추를 저울의 왼쪽에 올리는 경우
    cal(cnt + 1, abs(weight - chu_list[cnt - 1]))
    # 3. 추를 놓지 않는 경우
    cal(cnt + 1, weight)

dp = [[False] * 40001 for _ in range(31)]

cal(0, 0)

for bead in bead_list:
    if (dp[chu_cnt][bead]):
        print("Y", end=" ")
    else:
        print("N", end=" ")

