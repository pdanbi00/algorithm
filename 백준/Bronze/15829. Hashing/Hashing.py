L = int(input())
line = input()
ans = 0
for i in range(L):
  n = ord(line[i])-96
  ans += n * (31**i)
print(ans%1234567891)