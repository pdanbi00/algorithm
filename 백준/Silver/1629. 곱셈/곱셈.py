# 나머지 분배법칙 활용하는게 맞는데
# 지수도 나눠서 해야 됨
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
# 요런 느낌

# A, B, C = map(int, input().split())
# ans = 1
# for i in range(B):
#     ans = ((ans % C) * (A % C)) % C
# print(ans % C)

# 분할 정복을 통한 제곱수를 구하는 방식 사용
A, B, C = map(int, input().split())

def multi(a, n):
    if n == 1:
        return a % C
    else:
        tmp = multi(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C
print(multi(A, B))