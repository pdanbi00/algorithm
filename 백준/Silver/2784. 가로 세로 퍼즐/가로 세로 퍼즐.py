from itertools import permutations

board = [[0] * 3 for _ in range(3)]

words = []
for _ in range(6):
    word = input()
    words.append(word)
words.sort()

for perm in permutations(words, 3):
    arr = []
    for i in range(3):
        arr.append(perm[i])
        tmp = ''
        tmp += perm[0][i]
        tmp += perm[1][i]
        tmp += perm[2][i]
        arr.append(tmp)
    arr.sort()
    possible = True
    for i in range(6):
        if arr[i] != words[i]:
            possible = False
            break
    if possible:
        for i in range(3):
            print(perm[i])
        break
if not possible:
    print(0)