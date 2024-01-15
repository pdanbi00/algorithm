a, b = map(int, input().split())

# 최대공약수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 최소공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))