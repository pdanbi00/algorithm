address = input()
N = len(address)
separated_address = address.split(":")

answer = []
idx = 0
pre = 0
zero_idx = -1
cnt = 0
while idx < N:
    if address[idx] == ':':
        if idx + 1 < N and address[idx + 1] == ':':
            tmp = address[pre:idx]
            # print(tmp)
            if len(tmp) < 4:
                tmp = '0' * (4 - len(tmp)) + tmp
                cnt += 1
            answer.append(tmp)
            zero_idx = len(answer)
            idx += 2
            pre = idx
        else:
            tmp = address[pre:idx]
            # print(tmp)
            if len(tmp) < 4:
                tmp = '0' * (4 - len(tmp)) + tmp
            answer.append(tmp)
            if idx + 1 < N and address[idx+1] != ':':
                pre = idx + 1
            elif address[idx+1] == ':':
                pre = idx + 2
            idx += 1
    else:
        idx += 1
if pre < N:
    tmp = address[pre:N]
    # print(tmp)
    if len(tmp) < 4:
        tmp = '0' * (4 - len(tmp)) + tmp
    answer.append(tmp)

if len(answer) < 8:
    answer = answer[:zero_idx] + ['0000'] * (8-len(answer)) + answer[zero_idx:]
tmp = ''
for i in range(8):
    tmp += answer[i]
    if i < 7:
        tmp += ':'
print(tmp)