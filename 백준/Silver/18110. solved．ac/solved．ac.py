# round는 사사오입이 아니라 오사오입으로 처리함;;
# 오사오입 : 5미만 숫자는 내림. 5초과 숫자는 올림. 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수면 올림, 짝수면 내림\
# 거지같군
# 그래서 반올림하는 함수 따로 만들어줘야됨
import sys
input = sys.stdin.readline

def round2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
if N == 0:
    print(0)
else:
    score = [int(input()) for i in range(N)]
    if len(score) == 0:
        print(0)
    else:
        score.sort()
        count = round2(N*0.15)
        if count > 0:
            total = sum(score[count:-count])
            print(round2(total/(N-(2*count))))
        else:
            total = sum(score)
            print(round2(total/N))