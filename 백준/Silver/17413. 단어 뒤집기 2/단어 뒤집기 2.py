S = input()
N = len(S)
idx = 0
s = 0
e = 0

ans = ''
while idx < N:
    if S[idx] == '<':
        while idx < N and S[idx] != '>':
            ans += S[idx]
            idx += 1
        ans += S[idx]
    elif S[idx] != ' ':
        s = idx
        while idx < N and S[idx] != ' ' and S[idx] != '<':
            idx += 1
        idx -= 1
        e = idx
        tmp = S[s:e+1]
        ans += tmp[::-1]
    elif S[idx] == ' ':
        ans += ' '

    idx += 1
print(ans)