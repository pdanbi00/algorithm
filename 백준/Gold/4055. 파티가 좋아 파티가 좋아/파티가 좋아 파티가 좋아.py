tc = 0
while True:
    tc += 1
    p = int(input())
    if p == 0:
        break

    party = [(0, 0)]
    for _ in range(p):
        s, e = map(int, input().split())
        e -= 1
        if s > e:
            continue
        party.append((s, e))

    party.sort(key=lambda x : (x[1], -x[0]))

    cnt = 0
    for t in range(8, 24):
        for d in range(2):
            for i in range(len(party)):
                if party[i][0] <= t and party[i][1] >= t:
                    cnt += 1
                    party.pop(i)
                    break

    print(f'On day {tc} Emma can attend as many as {cnt} parties.')