info = dict()

for i in range(10):
    if i == 1:
        info[str(i)] = 2
    elif i == 0:
        info[str(i)] = 4
    else:
        info[str(i)] = 3

while True:
    N = input()
    if N == '0':
        break

    answer = 0
    answer += len(N) + 1

    for n in N:
        answer += info[n]

    print(answer)