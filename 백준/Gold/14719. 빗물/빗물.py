H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0

# 크작크로 되어야 됨
# 특정 위치를 기준으로 양옆에 자신보다 작은 높이의 블록이 있으면 해당 위치는 물이 고일 수 없음.
# 특정 위치에 물이 고이기 위해서는 자신보다 높은 블록으로 왼쪽과 오른쪽이 둘러쌓여있어야 함.
# 첫번째 칸이랑 마지막 칸은 물이 고일 수 없음

for i in range(1, W-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])

    compare = min(left_max, right_max)

    if blocks[i] < compare:
        answer += compare - blocks[i]

print(answer)