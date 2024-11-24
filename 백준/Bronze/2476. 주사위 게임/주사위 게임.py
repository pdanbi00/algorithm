ans = 0
N = int(input())
for _ in range(N):
    dice = list(map(int, input().split()))
    if dice[0] == dice[1] and dice[1] == dice[2]:
        tmp = 10000 + dice[0] * 1000
    elif dice[0] == dice[1]:
        tmp = 1000 + dice[0] * 100
    elif dice[0] == dice[2]:
        tmp = 1000 + dice[0] * 100
    elif dice[1] == dice[2]:
        tmp = 1000 + dice[1] * 100
    else:
        tmp = max(dice) * 100
    ans = max(ans, tmp)
print(ans)