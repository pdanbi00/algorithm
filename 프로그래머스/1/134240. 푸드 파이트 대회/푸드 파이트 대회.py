from collections import deque
def solution(food):
    answer = '0'
    N = len(food)
    # 1번 인덱스부터 홀수개면 -1개
    for i in range(N-1, 0, -1):
        cnt = food[i]
        if (cnt % 2 == 1):
            cnt -= 1
            
        cnt //= 2
        answer = str(i) * cnt + answer + str(i) * cnt
        
    # 1223330333221
    return answer