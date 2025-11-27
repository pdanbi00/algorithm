R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
rank = dict()
rank_list = []

for i in range(R):
    for j in range(C-2, 0, -1):
        if board[i][j] != '.':
            rank_list.append(((C-2)-j, board[i][j]))
            break

rank_list.sort()
pre = -1
idx = 0
for i in range(len(rank_list)):
    if int(rank_list[i][0]) != pre:
        idx += 1
        rank[int(rank_list[i][1])] = idx
        pre = int(rank_list[i][0])
    else:
        rank[int(rank_list[i][1])] = idx

for i in range(1, 10):
    print(rank[i])