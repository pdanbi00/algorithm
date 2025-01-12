num = list(input())
ans = 1

if num[0] == 'd':
    answer = 10
else:
    answer = 26
for i in range(1, len(num)):
    if num[i] == 'd':
        if num[i-1] == 'd':
            answer *= 9
        else:
            answer *= 10
    else:
        if num[i-1] == 'c':
            answer *= 25
        else:
            answer *= 26

print(answer)
