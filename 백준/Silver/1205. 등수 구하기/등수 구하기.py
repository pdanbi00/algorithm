N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    if N == P and score <= scores[-1]:
        print(-1)
    else:
        for i in range(N):
            if scores[i] <= score:
                print(i+1)
                break
        else:
            print(N+1)