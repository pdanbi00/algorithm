num1 = input()
num2 = input()

num_dict = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
char_dict = {1000:'M', 900 :'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

check = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

N = len(num1)
idx = 0
n1 = 0
while idx < N:
    if idx < N-1:
        tmp = num1[idx] + num1[idx+1]
        if tmp in check:
            n1 += num_dict[tmp]
            idx += 2
        else:
            n1 += num_dict[num1[idx]]
            idx += 1
    else:
        n1 += num_dict[num1[idx]]
        idx += 1

N = len(num2)
idx = 0
n2 = 0
while idx < N:
    if idx < N-1:
        tmp = num2[idx] + num2[idx+1]
        if tmp in check:
            n2 += num_dict[tmp]
            idx += 2
        else:
            n2 += num_dict[num2[idx]]
            idx += 1
    else:
        n2 += num_dict[num2[idx]]
        idx += 1
# print(n1, n2)
total = n1 + n2
print(total)

answer = ''

nums = list(char_dict.keys())
nums.sort(reverse=True)


char_cnt = {'V':0, 'L':0, 'D':0, 'IV':0, 'IX':0, 'XL':0, 'XC':0, 'CD':0, 'CM':0}
for k in nums:
    cnt = 0
    c = char_dict[k]
    while total >= k:
        if cnt >= 3:
            break

        if c in char_cnt and char_cnt[c] > 0:
            break

        if c == 'IV' and answer[-2:] == 'IX':
            break
        elif c == 'XL' and answer[-2:] == 'XC':
            break
        elif c == 'CM' and answer[-2:] == 'CD':
            break

        total -= k
        answer += c
        if c in char_cnt:
            char_cnt[c] += 1
        else:
            cnt += 1

print(answer)