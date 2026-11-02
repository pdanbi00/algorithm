def solution(players, callings):
    answer = []
    result = dict()
    for i in range(len(players)):
        result[players[i]] = i
        
    for call in callings:
        idx = result[call]
        result[call] -= 1
        result[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players