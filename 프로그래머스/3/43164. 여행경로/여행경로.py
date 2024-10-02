# dfs
def solution(tickets):
    answer = []
    tickets.sort(key=lambda x : (x[0], x[1]))
    
    # DFS
    def getPath(t, path):
        # 티켓을 다 썼다면 현재까지의 path 그대로 리턴
        if len(t) == 0:
            return path
        now = path[-1]
        valid_idx = -1
        
        # 남은 티켓 중에서 출발지가 현재 공항인 티켓 인덱스 찾기
        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break
        
        # 티켓이 남아있는데 갈 수 있는 공항이 없다는건 유효한 루트가 아닌거임
        if valid_idx == -1:
            return []
        
        while t[valid_idx][0] == now:
            next_path = getPath(t[:valid_idx] + t[valid_idx+1:], path + [t[valid_idx][1]])
            if next_path != []:
                return next_path
            valid_idx += 1
        return []
    return getPath(tickets, ['ICN'])