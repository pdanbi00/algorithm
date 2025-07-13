N, K = map(int, input().split())
answer = ['?'] * N
idx = 0
possible = True
alpha_set = set()
for _ in range(K):
    cnt, alpha = input().split()
    idx = (idx + int(cnt)) % N
    if answer[idx] == '?':
        if alpha not in alpha_set:
            answer[idx] = alpha
            alpha_set.add(alpha)
        else:
            possible = False
            break
    elif answer[idx] != alpha:
        possible = False
        break

if not possible:
    print("!")
else:
    ans = ''
    for i in range(N):
        ans += answer[(idx+(N-i)) % N]
    print(ans)