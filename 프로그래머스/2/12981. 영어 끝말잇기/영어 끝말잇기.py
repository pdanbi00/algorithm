def solution(n, words):
    answer = []
    used = set()
    N = len(words)
    cnt = 0
    
    for i in range(N):
        if words[i] in used:
            answer.append(i%n+1)
            if (i+1)%n > 0:
                answer.append(((i+1)//n + 1))
            else:
                answer.append((i+1)//n)
            
            break
        else:
            if i != 0:
                if words[i][0] != words[i-1][-1]:
                    answer.append(i%n+1)
                    if (i+1)%n > 0:
                        answer.append(((i+1)//n) + 1)
                    else:
                        answer.append((i+1)//n)
                    break
            used.add(words[i])

    if not answer:
        answer.append(0)
        answer.append(0)

    return answer