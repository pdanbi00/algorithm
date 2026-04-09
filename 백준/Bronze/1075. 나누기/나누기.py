N = input()
F = int(input())

front = N[:-2]
possible = []
for i in range(100):
    tmp = int(front) * 100 + i
    if tmp % F == 0:
        possible.append(str(tmp)[-2:])
        break
# possible.sort()
print(''.join(possible[0]))