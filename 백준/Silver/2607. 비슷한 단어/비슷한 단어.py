# 첫번째 단어보다 한 글자만 더 많거나 더 적거나 글자 개수는 일치하는데 글자가 다를 경우
N = int(input())
ans = 0
answer = input()
answer_arr = [0] * 26
for a in answer:
    answer_arr[ord(a) - 65] += 1
for _ in range(N-1):
    line = input()
    line_arr = [0] * 26
    for l in line:
        line_arr[ord(l) - 65] += 1
    more_cnt = 0
    less_cnt = 0
    possible = True
    for i in range(26):
        if answer_arr[i] - line_arr[i] >= 2 or answer_arr[i] - line_arr[i] <= -2:
            possible = False
            break
        if answer_arr[i] - line_arr[i] == 1:
            more_cnt += 1
        elif answer_arr[i] - line_arr[i] == -1:
            less_cnt += 1
    if not possible:
        continue
    if more_cnt == 0 and less_cnt == 0: # 구성이 동일한 경우
        ans += 1
    elif more_cnt == 1 and less_cnt == 0: # 한문자를 더해야하는 경우
        ans += 1
    elif more_cnt == 0 and less_cnt == 1: # 한 문자를 빼야하는 경우
        ans += 1
    elif more_cnt == 1 and less_cnt == 1: # 한 문자를 다른 문자로 바꿔야하는 경우
        ans += 1
print(ans)