sign = input()
possible = True
letters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

for s in sign:
    if s not in letters:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")