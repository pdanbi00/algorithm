def solution(bandage, health, attacks):
    answer = 0
    power = health
    heal = 0
    N = len(attacks)
    time = 0
    
    for i in range(N):
        t, attack = attacks[i]
        heal += t-1-time
        tmp = (heal // bandage[0]) * bandage[2] + (heal * bandage[1])
        power = min(health, power + tmp)
        
        time = t
        power -= attack
        heal = 0
        
        if power <= 0:
            answer = -1
            break
            
    if answer != -1:
        answer = power
        
        
    return answer