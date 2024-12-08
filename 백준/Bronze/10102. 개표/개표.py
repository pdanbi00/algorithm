V = int(input())
result = list(input())
a = result.count('A')
b = result.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')