S = list(input())
zero_cnt = 0
one_cnt = 0

for s in S:
    if s == '0':
        zero_cnt += 1
    else:
        one_cnt += 1
zero_cnt //= 2
one_cnt //= 2
ans = ''
# 0은 두고 1은 지우고
for i in range(len(S)):
    if S[i] == '0' and zero_cnt > 0:
        ans += '0'
        zero_cnt -= 1
    elif S[i] == '1' and one_cnt > 0:
        one_cnt -= 1
    elif S[i] == '1' and one_cnt == 0:
        ans += '1'

print(ans)