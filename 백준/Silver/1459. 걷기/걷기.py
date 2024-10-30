R, C, W, S = map(int, input().split())

# 이동할 수 있는 경우가 3가지가 있음
# 평행 이동만으로 이동
# 대각선으로만 이동하다가 마지막 한칸은 평행 이동
# 대각선이랑 평행이동 섞는 경우

# 평행이동
move1 = (R + C) * W

# 짝수 홀수에 따른 이동
if (R+C) % 2 == 0: # 대각선으로만 이동 가능
    move2 = max(R, C) * S
else: # 홀수일 경우 다 대각선으로 이동하고, 한칸은 평행으로
    move2 = (max(R, C) - 1) * S + W

# 대각선이랑 평행이동 섞어서 이동
move3 = (min(R, C) * S) + (max(R, C) - min(R, C)) * W

ans = min(move1, move2, move3)
print(ans)