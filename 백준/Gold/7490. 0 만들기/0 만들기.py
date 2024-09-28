T = int(input())

def check(idx, N, line):
    if idx == N:
        total = eval(line.replace(' ', ''))
        if total == 0:
            ans.append(line)
        return
    else:
        check(idx + 1, N, line + ' ' + str(idx+1))
        check(idx + 1, N, line + '+' + str(idx + 1))
        check(idx + 1, N, line + '-' + str(idx + 1))

for _ in range(T):
    N = int(input())
    ans = []

    check(1, N, '1')

    for a in ans:
        print(a)
    print()
