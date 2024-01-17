E, S, M = 1, 1, 1
year = 1
ans_E, ans_S, ans_M = map(int, input().split())
while True:
    if E == ans_E and S == ans_S and M == ans_M:
        print(year)
        break
    E += 1
    S += 1
    M += 1
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1
    year += 1