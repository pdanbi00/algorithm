mo = ['a', 'e', 'i', 'o', 'u']
def check(word):
    find = False
    for w in word:
        if w in mo:
            find = True
            break
    if not find:
        # print(1)
        return False

    if len(word) >= 3:
        for i in range(len(word)-2):
            if word[i] not in mo and word[i+1] not in mo and word[i+2] not in mo:
                # print(2)
                return False
            elif word[i] in mo and word[i+1] in mo and word[i+2] in mo:
                # print(2)
                return False

    if len(word) >= 2:
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                if word[i] != 'e' and word[i] != 'o':
                    # print(3)
                    return False

    return True

while True:
    word = input()
    if word == 'end':
        break
    result = check(word)
    print(f'<{word}> is ', end='')
    if result:
        print('acceptable.')
    else:
        print('not acceptable.')