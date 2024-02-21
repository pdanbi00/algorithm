# 아이디어 : 배열을 다 돌면서 연결된 사람들을 그래프로 나타냄
#           그리고 나서 진실을 아는 사람들로 시작해서 그래프 따라가면서 표시하고
#           파티마다 진실 들킬 수 있는 사람 있는지 확인해서 아무도 없으면 ans + 1
#           내가 놓친 부분은 파티마다 새롭게 진실을 아는 사람이 추가 된다는 부분을 빼먹어버림
# BFS
from collections import deque
N, M = map(int, input().split())
truth = list(map(int, input().split()))
graph = [[] for _ in range(N+1)] # 사람들 간 연결을 표시하는 그래프
know = [False for _ in range(N+1)] # 진실을 아는 사람 체크
parties = [] # 파티별 구성원 리스트
for i in range(M):
    party_info = list(map(int, input().split()))
    num = party_info[0]
    people = party_info[1:]
    parties.append(people)
    for i in range(num):
        for j in range(i+1, num): # 양방향으로
            graph[people[i]].append(people[j])
            graph[people[j]].append(people[i])
graph = [list(set(x)) for x in graph] # 중복제거
if len(truth) == 1:
    print(M)
else:
    know_truth_count = truth[0]
    know_truth_people = truth[1:]
    for true in know_truth_people:
        know[true] = True

    # 여기부터 이제 bfs
    def bfs(x):
        q = deque() # 진실을 아는 사람들 리스트
        q.append(x)
        while q:
            now = q.popleft()
            for next in graph[now]: # 진실을 아는 사람들이랑 관계 있는 사람들 중에
                if not know[next]: # 아직 진실을 모르면
                    know[next] = True # 이제 진실을 알게 되니깐 바꾸기
                    q.append(next) # 새롭게 진실을 알게된 사람으로부터 또 다시 탐색해야하니깐

    # 처음부터 진실을 아는 사람들
    for k in range(1, len(know)):
        if know[k]:
            bfs(k)

    # 0번 제외한 숫자 추출
    knows = [x for x in range(1, len(know)) if know[x]]

    cnt = 0
    for party in parties: # 각 파티에서
        if not (set(party) & set(knows)): # 파티에 참가한 사람이랑 진실을 아는 사람이랑 겹치는게 없으면
            cnt += 1
    print(cnt)
