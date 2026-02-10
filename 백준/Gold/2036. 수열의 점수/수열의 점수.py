import sys
input = sys.stdin.readline

N = int(input())
minus = []
plus = []
zero = 0
one = 0
for _ in range(N):
    num = int(input())
    if num == 1:
        one += 1
    else:
        if num > 0:
            plus.append(num)
        elif num < 0:
            minus.append(num)
        else:
            zero += 1

minus.sort()
plus.sort(reverse=True)
lm = len(minus)
lp = len(plus)

# print(minus, plus, zero, one)
answer = 0

if lm == 1:
    if zero == 0:
        answer += minus[-1]

    if lp == 1:
        answer += plus[-1]
    elif lp >= 2:
        if lp % 2 == 1:
            answer += plus[-1]
            for i in range(0, lp - 1, 2):
                answer += plus[i] * plus[i + 1]
        else:
            for i in range(0, lp, 2):
                answer += plus[i] * plus[i + 1]
else:
    if lm % 2 == 0:
        for i in range(0, lm, 2):
            answer += minus[i] * minus[i+1]

        if lp == 1:
            answer += plus[-1]
        elif lp >= 2:
            if lp % 2 == 1:
                answer += plus[-1]
                for i in range(0, lp - 1, 2):
                    answer += plus[i] * plus[i + 1]
            else:
                for i in range(0, lp, 2):
                    answer += plus[i] * plus[i + 1]

    else:
        for i in range(0, lm-1, 2):
            answer += minus[i] * minus[i + 1]

        if lp == 1:
            answer += plus[-1]
        elif lp >= 2:
            if lp % 2 == 1:
                answer += plus[-1]
                for i in range(0, lp - 1, 2):
                    answer += plus[i] * plus[i + 1]
            else:
                for i in range(0, lp, 2):
                    answer += plus[i] * plus[i + 1]

        if zero == 0:
            answer += minus[-1]

print(answer + one)


'''
2
1
2
'''