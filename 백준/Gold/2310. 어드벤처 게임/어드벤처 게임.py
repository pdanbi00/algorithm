def dfs(r_num, money):
    global ans

    if r_num == N-1:
        ans = True
        return

    if ans:
        return

    for next_room in board[r_num]:
        if visited[next_room] == False:
            if room[next_room][0] == 'E':
                visited[next_room] = True
                dfs(next_room, money)
                visited[next_room] = False

            elif room[next_room][0] == 'L':
                if money < room[next_room][1]:
                    money = room[next_room][1]
                visited[next_room] = True
                dfs(next_room, money)
                visited[next_room] = False

            elif room[next_room][0] == 'T':
                if money - room[next_room][1] >= 0:
                    visited[next_room] = True
                    dfs(next_room, money - room[next_room][1])
                    visited[next_room] = False

while True:
    N = int(input())
    if N == 0:
        break
    board = [[] for _ in range(N)]
    room = []
    for i in range(N):
        arr = list(input().split())
        arr = arr[:-1]
        room.append((arr[0], int(arr[1])))
        for j in range(2, len(arr)):
            board[i].append(int(arr[j]) - 1)

    ans = False
    visited = [False] * N
    visited[0] = True
    if room[0][0] == 'E':
        dfs(0, 0)
    elif room[0][0] == 'L':
        dfs(0, room[0][1])

    if ans:
        print('Yes')
    else:
        print('No')