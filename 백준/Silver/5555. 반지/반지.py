target = list(input())

N = int(input())

ans = 0

for _ in range(N):

    ring = list(input())

    tmp = ''

    for i in range(2):

        for j in range(len(ring)):

            tmp += ring[j]

            

    for i in range(len(ring)):

        cnt = 0

        for j in range(len(target)):

            if target[j] == tmp[i+j]:

                cnt += 1

        if cnt == len(target):

            ans += 1

            break

            

print(ans)