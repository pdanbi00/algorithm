# import sys
# input = sys.stdin.readline
# N = int(input())
# problems = []
# levels = []
# problemsLevel = dict() # 각 문제에 해당하는 레벨(key : 문제번호, value : 레벨)
# levelProblem = dict() # 각 레벨에 해당하는 문제(key : 레벨, value : 문제)
#
# for _ in range(N):
#     p, l = map(int, input().split())
#     problems.append(p)
#     levels.append(l)
#     problemsLevel[p] = l
#     if l in levelProblem:
#         levelProblem[l].append(p)
#     else:
#         levelProblem[l] = [p]
#
# problems.sort()
# levels.sort()
# for k, v in levelProblem.items():
#     v.sort()
#
# M = int(input())
# for _ in range(M):
#     command = list(input().rstrip().split())
#     if command[0] == 'recommend':
#         if int(command[1]) == 1:
#             print(levelProblem[levels[-1]][-1])
#         else:
#             print(levelProblem[levels[0]][0])
#
#     elif command[0] == 'add':
#         p, l = int(command[1]), int(command[2])
#         problems.append(p)
#         levels.append(l)
#         problems.sort()
#         levels.sort()
#         problemsLevel[p] = l
#         if l in levelProblem:
#             levelProblem[l].append(p)
#             levelProblem[l].sort()
#         else:
#             levelProblem[l] = [p]
#
#     else:
#         p = int(command[1])
#         l = problemsLevel[p]
#         del problemsLevel[p]
#         levelProblem[l].remove(p)
#         problems.remove(p)
#         levels.remove(l)
#
# '''
# 3
# 1000 1
# 1001 1
# 1002 1
# 8
# recommend 1
# add 1003 1
# recommend 1
# solved 1003
# recommend 1
# recommend -1
# add 1 1
# recommend -1
# '''


# minHeap과 maxHeap을 모두 사용해야 됨
from heapq import heappush, heappop
import sys
from collections import defaultdict

input = sys.stdin.readline

minHeap = []
maxHeap = []
problems = defaultdict(int)
N = int(input())
for _ in range(N):
    p, l = map(int, input().split())
    heappush(minHeap, (l, p))
    heappush(maxHeap, (-l, -p))
    problems[p] = l

M = int(input())
for _ in range(M):
    command = list(input().split())

    if command[0] == "recommend":
        # 어려운 문제 추천
        if command[1] == '1':
            # solved[어려운 문제]가 입력받은 난이도와 다를 경우 이미 푼 문제
            while problems[abs(maxHeap[0][1])] != abs(maxHeap[0][0]):
                heappop(maxHeap)
            print(-maxHeap[0][1])
        # 쉬운 문제 추천
        else:
            # solved[쉬운 문제]가 입력받은 난이도와 다를 경우 이미 푼 문제
            while problems[minHeap[0][1]] != minHeap[0][0]:
                heappop(minHeap)
            print(minHeap[0][1])

    elif command[0] == "add":
        p, l = int(command[1]), int(command[2])
        heappush(maxHeap, (-l, -p))
        heappush(minHeap, (l, p))
        problems[p] = l
    elif command[0] == "solved":
        problems[int(command[1])] -= 1