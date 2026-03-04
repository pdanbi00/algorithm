N = int(input())
line = ''
for i in range(1, N+1):
    line += str(i)
N = str(N)
l = len(N)
for i in range(len(line)):
    if line[i] == N[0]:
        cnt = 0
        for j in range(l):
            if line[i+j] == N[j]:
                cnt += 1
            else:
                break
        if cnt == l:
            print(i+1)
            break