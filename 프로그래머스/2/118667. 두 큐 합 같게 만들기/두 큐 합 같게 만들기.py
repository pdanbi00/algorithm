# 아이디어 : 배열 크기는 같다 했음. 고로 두개 합 다 더해서 2로 나눴을 때 홀수면 일단 제낌. 짝수일 경우에 자 두 합이 같으면? 그게 답임. 첫번째 큐의 합이 더 크면? 첫번째꺼에서 빼서 두번째꺼에 넣어줘야됨. 두번째 큐의 합이 더 크면? 두번째꺼에서 빼서 첫번째꺼에 넣어줘야됨. 자 이 반복을 언제까지 하냐? 첫번째 큐에 있던거 다 빼서 두번째꺼에 넣어서 다시 첫번째꺼가 원상복귀 되려면 총 4n번 동안 push, pop이 이뤄짐. 이해 안되면 그림 그려보셈

from collections import deque

def solution(queue1, queue2):
    answer = 0 # pop, insert한 횟수
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    max_banbok = (len(queue1) + len(queue2)) * 2 # 최대 반복
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    
    if total % 2 == 1:
        return -1
    
    while True:
        if sum1 == sum2:
            break
        elif sum1 > sum2:
            target = queue1.popleft()
            queue2.append(target)
            sum1 -= target
            sum2 += target
            answer += 1
        else: # queue2의 합이 queue1의 합 보다 큰 경우
            target = queue2.popleft()
            queue1.append(target)
            sum1 += target
            sum2 -= target
            answer += 1
        if answer == max_banbok:
            return -1
        
    return answer