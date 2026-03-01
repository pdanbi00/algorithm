# # 정규표현식
# import re
#
# word = input()
# pattern = re.compile('(100+1+|01)+')
#
# res = pattern.fullmatch(word)
#
# if res:
#     print("SUBMARINE")
# else:
#     print("NOISE")

word = input()

i = 0
N = len(word)
possible = True

while i < N:
    if i >= N-1:
        possible = False
        break

    elif word[i:i+2] == '01':
        i += 2
    elif word[i:i+2] == '10':
        i += 2
        if word[i] == '1':
            possible = False
            break

        while i < N:
            if word[i] == '1':
                break
            else:
                i += 1
        else:
            possible = False # 100 다음에는 1이 하나는 와야 됨.
            break

        while i < N and word[i] == '1':
            if word[i] == '0':
                break
            else:
                i += 1

        if i < N-1 and word[i:i+2] == '00':
            i -= 1
        if word[i-1] == '0':
            possible = False
            break
    else:
        possible = False
        break

if possible:
    print("SUBMARINE")
else:
    print("NOISE")