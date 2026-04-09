N = input()
F = int(input())
# print(F)
front = N[:-2]
back = N[-2:]
possible = []
for i in range(100):
    if int(back) + i >= 100:
        break

    tmp = int(front) * 100 + int(back) + i
    if tmp % F == 0:
        # print(tmp, str(tmp)[-2:])
        possible.append(str(tmp)[-2:])

for i in range(100):
    if int(back) - i < 0:
        break

    tmp = int(front) * 100 + int(back) - i
    # print(tmp%F)
    if tmp % F == 0:
        # print(tmp, str(tmp)[-2:])
        possible.append(str(tmp)[-2:])

possible.sort()
# print(possible)
print(''.join(possible[0]))