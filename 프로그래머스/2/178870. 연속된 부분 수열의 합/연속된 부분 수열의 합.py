def solution(sequence, k):
    answer = []
    s, e = 0, 0
    tmp = sequence[0]
    while s <= e and e < len(sequence):
        # print(s, e, tmp)
        if tmp == k:
            answer.append((s, e, e-s+1))
            tmp -= sequence[s]
            s += 1
            
        elif tmp > k:
            tmp -= sequence[s]
            s += 1
            
        else:
            e += 1
            if e < len(sequence):
                tmp += sequence[e]
            
    # print('-------------end------')
    # print(s, e, tmp)
    # print(answer)
    answer.sort(key = lambda x : (x[2], x[0]))
    return [answer[0][0], answer[0][1]]