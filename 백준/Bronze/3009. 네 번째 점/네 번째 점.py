r_dict = {}
c_dict = {}
for _ in range(3):
    r, c = map(int, input().split())
    if r in r_dict:
        r_dict[r] += 1
    else:
        r_dict[r] = 1

    if c in c_dict:
        c_dict[c] += 1
    else:
        c_dict[c] = 1

ans = []
for k, v in r_dict.items():
    if v % 2 == 1:
        ans.append(k)

for k, v in c_dict.items():
    if v % 2 == 1:
        ans.append(k)
print(*ans)