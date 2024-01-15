def is_prime(a):
    if a < 2:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True

N = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if is_prime(num):
        count += 1
print(count)