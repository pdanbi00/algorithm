def solution(n, k, cmd):
    answer = ''
    '''
    링크드 리스트였음...
    딕셔너리로 해서 key는 인덱스, value는 앞 인덱스랑 뒷 인덱스
    '''
    
    N = len(cmd)
    linked_list = {i : [i-1, i+1] for i in range(n)}
    data = ['O'] * n
    deleted = []
    
    for i in range(N):
        command = cmd[i].split()
        
        if command[0] == 'U':
            for _ in range(int(command[1])):
                k = linked_list[k][0]
        elif command[0] == 'D':
            for _ in range(int(command[1])):
                k = linked_list[k][1]
        elif command[0] == 'C':
            prev, nxt = linked_list[k]
            data[k] = 'X'
            deleted.append((prev, k, nxt))
            
            if nxt == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]
                
            
            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        else:
            prev, value, nxt = deleted.pop()
            data[value] = 'O'
            
            if prev == -1:
                linked_list[nxt][0] = value
            elif nxt == n:
                linked_list[prev][1] = value
            else:
                linked_list[prev][1] = value
                linked_list[nxt][0] = value
            
    
    answer = ''.join(data)
    return answer