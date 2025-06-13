import decimal
decimal.getcontext().prec = 1000  # 전체 연산 정밀도를 소수점 이하 1000자리까지 설정

T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    n = input()  # 입력 숫자 (문자열)
    num = decimal.Decimal(n + '.0000000000')  # Decimal로 변환 (정확도 보장)
    pow = decimal.Decimal('1') / decimal.Decimal('3')  # 1/3 (세제곱근을 위해)
    d = decimal.Decimal(num ** pow)  # 세제곱근 계산
    # d = round(d, 500)  # 소수점 이하 500자리까지 반올림
    # round는 float 형 함수 라서 부동소수점 문제가 발생할 수 있음. 그래서 개선하는 방법은
    d = d.quantize(decimal.Decimal('1.' + '0' * 500)) # 소수점 아래 500자리까지 자르는건데 정확히 표현된 개체여야해서 '1.'을 붙임. '2.'으로 해도 됨. 근데 '0.'으로 하면 전체가 0으로 인식되어서 안됨
    d = decimal.Decimal(d).quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)  # 소수점 이하 10자리까지만 출력
    print(d)
