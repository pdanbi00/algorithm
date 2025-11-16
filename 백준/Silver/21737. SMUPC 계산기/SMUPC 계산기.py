def find_num():
    global idx
    num = ''
    while idx < len(calc):
        if calc[idx] not in ('S', 'M', 'U', 'P', 'C'):
            num += calc[idx]

        else:
            break
        idx += 1
    if num == '':
        return 0
    return int(num)

N = int(input())
calc = list(input())

tmp = int(calc[0])

if 'C' not in calc:
    print("NO OUTPUT")
else:
    idx = 0
    tmp = find_num()

    while idx < len(calc):
        if calc[idx] == 'S':
            idx += 1
            result = find_num()
            tmp -= result
        elif calc[idx] == 'M':
            idx += 1
            result = find_num()
            tmp *= result
        elif calc[idx] == 'U':
            idx += 1
            result = find_num()
            if tmp < 0 and result > 0:
                tmp *= -1
                tmp //= result
                tmp *= -1
            else:
                tmp //= result

        elif calc[idx] == 'P':
            idx += 1
            result = find_num()
            tmp += result
        elif calc[idx] == 'C':
            print(tmp, end=" ")
            idx += 1
        else:
            find_num()
'''
2
000232C38S
'''