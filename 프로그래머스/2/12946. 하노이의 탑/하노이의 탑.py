def hanoi(start, end, tmp, cnt, answer): # 시작 기둥 번호, 끝 기둥 번호, 남는 기둥 번호, 옮겨야하는 원판 수, 정답 배열
    if cnt == 1:
        answer.append([start, end])
    else:
        # 가장 아래 원판 제외한 나머지 cnt-1개를 남는 기둥으로 옮기기
        hanoi(start, tmp, end, cnt-1, answer)
        # 가장 아래 원판을 도착 기둥으로 옮기기
        hanoi(start, end, tmp, 1, answer)
        # 남는 기둥에 있던 cnt-1개의 원판을 도착 기둥으로 옮기기
        hanoi(tmp, end, start, cnt-1, answer)
        
    return answer

def solution(n):
    answer = hanoi(1, 3, 2, n, [])
    
    return answer

'''
dp? 재귀 d[i-1]을 2번으로 옮기고 d[i]를 3번으로 옮기고 d[i-1]을 다시 2번으로 옮기기

dp[1] = 1
dp[2] = 3
dp[3] = 7

dp[2] + 2?
'''