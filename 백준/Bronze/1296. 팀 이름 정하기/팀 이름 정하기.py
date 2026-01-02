name = input()
N = int(input())
team_name = []
for _ in range(N):
    team_name.append(input())

L = 0
O = 0
V = 0
E = 0
for n in name:
    if n == 'L':
        L += 1
    elif n == 'O':
        O += 1
    elif n == 'V':
        V += 1
    elif n == 'E':
        E += 1

max_point = -1
answer = []
for name in team_name:
    new_L = L
    new_O = O
    new_V = V
    new_E = E
    for n in name:
        if n == 'L':
            new_L += 1
        elif n == 'O':
            new_O += 1
        elif n == 'V':
            new_V += 1
        elif n == 'E':
            new_E += 1
    tmp = ((new_L + new_O) * (new_L+new_V) * (new_L+new_E) * (new_O+new_V) * (new_O+new_E) * (new_V+new_E)) % 100
    if tmp > max_point:
        answer = [name]
        max_point = tmp
    elif tmp == max_point:
        answer.append(name)
answer.sort()
print(answer[0])