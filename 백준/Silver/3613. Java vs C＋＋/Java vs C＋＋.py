line = input()

possible = True
big = False # 대문자 있는지
for a in line:
    if a != '_' and ord(a) - 97 < 0:
        big = True
        break

if big and '_' in line:
    # print(11111111)
    answer = "Error!"
elif line[-1] == '_' or line[0] == '_':
    # print(2222222222)
    answer = "Error!"
elif line[0].isupper():
    # print(3333333333)
    answer = "Error!"
else:
    if big: # 자바에서 c++형식으로 변환
        answer = ''
        for i in range(len(line)):
            if line[i].isupper():
                answer += '_'
                answer += line[i].lower()
            else:
                answer += line[i]

    else:
        answer = ''
        idx = 0
        while idx < len(line):
            if line[idx] == '_':
                idx += 1
                if idx < len(line):
                    if line[idx] == '_': # '_'이 2개 연속일 경우 땡
                        # print(444444444)
                        answer = "Error!"
                        break
                    answer += line[idx].upper()
            else:
                answer += line[idx]
            idx += 1

print(answer)

'''
long_and___mnemonic_identifier
'''