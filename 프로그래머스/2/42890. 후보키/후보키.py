from itertools import combinations

def solution(relation):
    N = len(relation[0])
    candidate_key = []
    arr = [i for i in range(N)]
    for i in range(1, N+1):
        for combi in combinations(arr, i): # 후보키가 될 수 있는 모든 key 조합
            temp = []
            for r in relation:
                curr = [r[c] for c in combi] # 현재 후보키 조합에 해당하는 데이터
                if curr in temp: # 유일성을 만족하지 못하는 경우
                    break
                else:
                    temp.append(curr)
            if len(temp) == len(relation):
                for ck in candidate_key:
                    if set(ck).issubset(set(combi)):
                        break
                else:
                    candidate_key.append(combi)

    return len(candidate_key)