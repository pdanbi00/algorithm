RE = PT = CC = EA = TB = CM = EX = 0
cnt = 0

while True:
    try:
        line = list(input().split())

        for a in line:
            cnt += 1
            if a == "Re":
                RE += 1
            elif a == "Pt":
                PT += 1
            elif a == "Cc":
                CC += 1
            elif a == "Ea":
                EA += 1
            elif a == "Tb":
                TB += 1
            elif a == "Cm":
                CM += 1
            elif a == "Ex":
                EX += 1
    except:
        break

print('Re', RE, '{:.2f}'.format(RE / cnt))
print('Pt', PT, '{:.2f}'.format(PT / cnt))
print('Cc', CC, '{:.2f}'.format(CC / cnt))
print('Ea', EA, '{:.2f}'.format(EA / cnt))
print('Tb', TB, '{:.2f}'.format(TB / cnt))
print('Cm', CM, '{:.2f}'.format(CM / cnt))
print('Ex', EX, '{:.2f}'.format(EX / cnt))
print(f'Total {cnt} 1.00')