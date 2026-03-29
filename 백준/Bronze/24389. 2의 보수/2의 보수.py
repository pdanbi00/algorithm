N = int(input())
com = (N ^ ((1 << 32) - 1)) + 1
print(bin(N ^ com).count('1'))