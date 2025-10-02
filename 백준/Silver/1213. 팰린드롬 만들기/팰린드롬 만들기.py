# 문장 길이가 짝수면 다 짝수개가 있어야 됨
# 문장 길이가 홀수면 문자 하나는 홀수개 있어야 됨.

words = list(input())
N = len(words)

words_dict = dict()
for w in words:
    if w in words_dict:
        words_dict[w] += 1
    else:
        words_dict[w] = 1

cnt = 0
alpha = []
odd_alpha = []

for k, v in words_dict.items():
    if v % 2 == 1:
        odd_alpha.append(k)
        alpha.append(k)
        cnt += 1
    else:
        alpha.append(k)
#
# print(alpha)
# print(odd_alpha)

if (N % 2 == 0 and cnt > 0) or (N % 2 == 1 and cnt > 1):
    answer = "I'm Sorry Hansoo"
else:
    alpha.sort()
    answer = [''] * N
    if cnt == 1:
        answer[N//2] = odd_alpha[0]
        words_dict[odd_alpha[0]] -= 1

    idx = 0
    cnt = 0
    while idx < N//2:
        w = alpha[cnt]
        for _ in range(words_dict[w] // 2):
            answer[idx] = w
            answer[N-1-idx] = w
            idx += 1
        cnt += 1
    answer = "".join(answer)
print(answer)