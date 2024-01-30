from collections import deque
MAX = 2000
S = int(input())
board = [[-1] * (MAX+1) for _ in range(MAX+1)]
screen = 1
clipboard = 0
board[screen][clipboard] = 0
q = deque()
q.append((screen, clipboard))
while q:
    screen, clipboard = q.popleft()
    if screen == S:
        print(board[screen][clipboard])
        break
    # 1번 연산. 화면꺼 모두 복사해서 클립보드에 저장
    if 0 <= screen <= MAX:
        n_clipboard = screen
        if board[screen][n_clipboard] == -1:
            q.append((screen, n_clipboard))
            board[screen][n_clipboard] = board[screen][clipboard] + 1
    # 2번 연산. 클립보드에 있는거 다 화면에 붙여넣기. 근데 클립보드 비어있으면 안됨
    if 0 <= screen+clipboard <= MAX and 0 < clipboard <= MAX:
        n_screen = screen+clipboard
        if board[n_screen][clipboard] == -1:
            q.append((n_screen, clipboard))
            board[n_screen][clipboard] = board[screen][clipboard] + 1
    # 3번 연산. 화면에 있는거 하나 삭제
    if 0 <= screen - 1 <= MAX and 0 <= clipboard <= MAX:
        n_screen = screen - 1
        if board[n_screen][clipboard] == -1:
            q.append((n_screen, clipboard))
            board[n_screen][clipboard] = board[screen][clipboard] + 1