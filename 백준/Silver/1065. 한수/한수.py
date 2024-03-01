N = int(input())
cnt = 0
for i in range(1, N+1):
    num = str(i)
    not_answer = False
    if len(num) >= 2:
        diff = int(num[0]) - int(num[1])
        for j in range(1, len(num)-1):
            if int(num[j]) - int(num[j+1]) != diff:
                not_answer = True
                break
    if not not_answer:
        cnt += 1
print(cnt)