N = int(input())
vote = [int(input()) for _ in range(N)]

me = vote[0]

if N == 1:
    print(0)
else:
    vote = sorted(vote[1:], reverse=True)
    cnt = 0
    if me <= vote[0]:
        while True:
            vote[0] -= 1
            cnt += 1
            me += 1
            vote.sort(reverse=True)
            if me > vote[0]:
                break

    print(cnt)