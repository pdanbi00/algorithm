from math import sqrt
prime_nums = set()
def checkPrime(num):
    for j in range(2, int(sqrt(num))+1):
        if num % j == 0:
            return False
    else:
        prime_nums.add(num)
        return True

def power(a, p):
    mod = p
    res = 1
    while p:
        if p & 1 == 1:
            res = (res * a) % mod
        p >>= 1
        a = (a * a) % mod
    return res

while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break

    if p in prime_nums:
        print("no")
    else:
        result = checkPrime(p)
        if result:
            print("no")
        else:
            if power(a, p) == a:
                print("yes")
            else:
                print("no")