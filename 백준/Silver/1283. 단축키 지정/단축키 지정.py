N = int(input())
ans = []
keys = []
for _ in range(N):
    key = input().split()
    possible = False
    for i in range(len(key)):
        a = key[i][0].lower()
        # print(a)
        if a not in keys:
            keys.append(a)
            tmp = ''
            for k in range(i):
                for p in range(len(key[k])):
                    tmp += key[k][p]
                tmp += ' '
            tmp += '['
            tmp += key[i][0]
            tmp += ']'
            tmp += key[i][1:]
            tmp += ' '
            for k in range(i+1, len(key)):
                for p in range(len(key[k])):
                    tmp += key[k][p]
                tmp += ' '
            ans.append(tmp)
            possible = True
            break
    if not possible:
        for i in range(len(key)):
            for j in range(len(key[i])):
                a = key[i][j].lower()
                # print(a)
                if a not in keys:
                    keys.append(a)
                    tmp = ''
                    for k in range(i):
                        for p in range(len(key[k])):
                            tmp += key[k][p]
                        tmp += ' '
                    for p in range(j):
                        tmp += key[i][p]
                    tmp += '['
                    tmp += key[i][j]
                    tmp += ']'
                    for p in range(j+1, len(key[i])):
                        tmp += key[i][p]
                    tmp += ' '
                    for k in range(i+1, len(key)):
                        for p in range(len(key[k])):
                            tmp += key[k][p]
                        tmp += ' '

                    ans.append(tmp)
                    possible = True
                    break
            if possible:
                break
        if not possible:
            ans.append(' '.join(key))
for i in range(N):
    print(ans[i])