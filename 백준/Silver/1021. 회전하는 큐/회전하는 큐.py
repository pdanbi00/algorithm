from collections import deque
N, M = map(int, input().split())
index = list(map(int, input().split()))
q = deque(i for i in range(1, N+1))

cnt = 0 # 2번 연산, 3번 연산 수행하는 횟수 세기
for i in index:
    while True:
        if q[0] == i: # q의 첫번째 값이 뽑아내려는 값이랑 같으면 1번 작업 수행
            q.popleft()
            break
        else:
            # 뽑으려는 수의 위치가 dq의 길이를 반으로 나눈 것 보다 작으면 왼쪽으로 회전 시키기
            if q.index(i) < (len(q) / 2):
                while q[0] != i:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)