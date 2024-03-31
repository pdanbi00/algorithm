def compare(board, key, r, c, M, N):
    answer = True
    # r, c는 key 시작 좌표
    # M은 키 크기
    
    for i in range(M):
        for j in range(M):
            board[r+i][c+j] += key[i][j]
    
    for i in range(N):
        if not answer:
            break
        for j in range(N):
            if board[M+i][M+j] != 1: # 홈(0)이랑 돌기(1) 합치면 1이니깐
                answer = False
                break
    # key 더해진 board에서 다시 key 빼기
    for i in range(M):
        for j in range(M):
            board[r+i][c+j] -= key[i][j]    
    return answer
    

def solution(key, lock):
    # lock 배열을 3배 확장 시켜서 key 만큼씩 확인하면서 겹치는지 확인
    N = len(lock)
    M = len(key)
    board = [[0] * (N + 2*M) for _ in range(N+2*M)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    
    for i in range(4):
        key = operation(key)
                       
        for i in range(1, N+M): # 1에서 시작하는 이유는 0에서 시작하면 key랑 lock이랑 한나도 안겹쳐서 의미 업승.N+M도 겹치는 부분 없어서 
            for j in range(1, N+M):
                if compare(board, key, i, j, M, N):
                    return True
    return False

def operation(key): # 오른쪽으로 90도 이걸 4번 반복하면 됨.
    n = len(key)
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = key[n-1-j][i]
    return arr