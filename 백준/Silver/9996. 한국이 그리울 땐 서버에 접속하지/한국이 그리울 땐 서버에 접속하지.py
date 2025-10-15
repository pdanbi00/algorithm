N = int(input())
target = list(input())
for _ in range(N):
    words = list(input())
    if len(target) - 1 > len(words):
        print("NE")
        continue

    possible = True
    for i in range(len(target)):
        if target[i] == '*':
            break

        if target[i] != words[i]:
            possible = False
            break

    if possible:
        # print('prefix possible')
        for i in range(len(target)):
            if target[len(target)-1-i] == '*':
                break
            # print(target[len(target)-1-i], words[len(words)-1-i])
            if target[len(target)-1-i] != words[len(words)-1-i]:
                possible = False
                break

    if possible:
        print("DA")
    else:
        print("NE")


'''
5
ca*e
case
cake
cave
dave
kate
'''