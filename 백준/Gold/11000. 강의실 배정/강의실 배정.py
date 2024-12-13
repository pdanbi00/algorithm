import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
lecture.sort()

room = []
heappush(room, lecture[0][1]) # 첫번째 강의 끝나는 시간
# 강의실에서 진행하고 있는 수업의 종료 시간이 지금 시작하려는 시간보다 작거나 같아야 됨.

# 지금 사용중인 강의실 중에서도 제일 먼저 시작한 강의의 종료시간이랑 비교하면서 진행해야하기 때문에 우선순위 큐 사용
answer = 0
for i in range(1, N):
    # 강의 시작시간이 현재 강의나는 시간 보다 이르면
    if lecture[i][0] < room[0]:
        heappush(room, lecture[i][1]) # 새로운 강의실 배정
    else:
        heappop(room) # 기존 강의 종료.
        heappush(room, lecture[i][1])
    answer = max(answer, len(room))
print(answer)