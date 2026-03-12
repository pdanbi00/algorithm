# 소시지 N개를 이어붙이면 M-1번 칼질이 필요함.(최악의 경우)
# N이 M의 배수이면 칼질은 필요 없음.
# 즉, M - GCD(N, M)번의 칼질이 필요함.

def GCD(a, b) :
    # a, b에 대해서 a = bq + r이라고 하면
    # a, b의 최대공약수는 b, r의 최대공약수랑 같음

    if b == 0:
        return a
    return (GCD(b, a%b))

N, M = map(int, input().split())
print(M-GCD(N,M))
# N = 3, M = 12이면 GCD(N, M) = 3
# 즉, 3개의 소시지를 4명씩 배분하면 됨. 4-1번의 칼질이 3개의 소시지니깐 9번 칼질
# (M/gcd - 1) * gcd