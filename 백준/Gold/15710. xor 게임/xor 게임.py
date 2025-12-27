a, b, n = map(int, input().split())
mod = 1000000007
# print(2 ** 31)

def power(x, y):
    # x에 y거듭제곱 한 것을 mod로 나눈 나머지
    result = 1
    x %= mod
    while y:
        if y % 2:
            result = (result * x) % mod
        x = (x * x) % mod
        y //= 2
    return result

print(power((2 ** 31), n-1))