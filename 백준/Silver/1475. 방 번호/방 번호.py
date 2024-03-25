N = input()
dict = {}
for i in N:
    if i == '9':
        if '6' in dict:
            dict['6'] += 1
        else:
            dict['6'] = 1
    else:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
if '6' in dict:
    if dict['6'] % 2 == 1:
        dict['6'] = dict['6'] // 2 + 1
    else:
        dict['6'] //= 2
m = 0
for k, v in dict.items():
    if v > m:
        m = v
print(m)