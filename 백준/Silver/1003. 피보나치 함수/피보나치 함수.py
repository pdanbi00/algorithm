def fib(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i]+zero[i-1])
            one.append(one[i]+one[i-1])
    print(zero[n], one[n])
T = int(input())
nums = [int(input()) for _ in range(T)]
for num in nums:
    fib(num)
