N = int(input())
files = [list(input()) for _ in range(N)]

if N == 1:
    print(''.join(files[0]))
else:
    answer = ''
    for i in range(len(files[0])):
        cnt = 0
        for j in range(N):
            if files[j][i] == files[0][i]:
                cnt += 1
            else:
                break
        if cnt == N:
            answer += files[0][i]
        else:
            answer += '?'

    print(answer)