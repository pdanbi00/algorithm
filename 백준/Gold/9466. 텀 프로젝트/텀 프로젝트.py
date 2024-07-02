import sys
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(idx):
    global ans

    visited[idx] = True # 일단 나부터 시작
    team.append(idx)
    student = students[idx] # 다음 사람 지목
    if visited[student]: # 지목한 사람이 이미 방문한 사람이면
        if student in team: # 그 사람이 팀 후보에 있으면
            # 그 사람부터 이후에 들어온 사람들은 한 팀
            ans -= len(team[team.index(student):])
    else:
        dfs(student)


for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    ans = n
    # 일단 자기 자신 골랐으면 그냥 한 팀으로 빠짐
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)
    print(ans)
