N = int(input())
X = int(input())

result = (N * (100-X)) / 100
answer = (N / result * 100) - 100
print(round(answer, 6))
'''
result * x  = N
x = 100 - (N / result * 100)
'''