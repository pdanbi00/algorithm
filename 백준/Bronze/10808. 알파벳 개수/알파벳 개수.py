s_arr = input()
alpha = [0] * 26
for s in s_arr:
    alpha[ord(s) - 97] += 1
print(*alpha)