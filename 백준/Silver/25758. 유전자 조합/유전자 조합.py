N = int(input())
DNA = list(input().split())

# 첫번째 유전자로 'A'에서 'Z까지 하나를 고정했을 때 다른 형질로 골라질 수 있는 경우 모두 탐색
first = set()
second = set()
alpha_f_dict = dict()
alpha_s_dict = dict()

for f, s in DNA:
    first.add(f)
    second.add(s)
    if f in alpha_f_dict:
        alpha_f_dict[f] += 1
    else:
        alpha_f_dict[f] = 1

    if s in alpha_s_dict:
        alpha_s_dict[s] += 1
    else:
        alpha_s_dict[s] = 1

ans = set()
for f in first:
    for s in second:
        tmp = f + s
        if tmp in DNA and (alpha_f_dict[f] > 1 or alpha_s_dict[s] > 1):
            if f >= s:
                ans.add(f)
            else:
                ans.add(s)

        elif tmp not in DNA:
            if f >= s:
                ans.add(f)
            else:
                ans.add(s)

        if len(ans) ==  26:
            break
    if len(ans) == 26:
        break

ans = list(ans)
ans.sort()
print(len(ans))
print(*ans)