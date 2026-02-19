distance = int(input())
length = len(str(distance))
result = 0
for i in range(length):
    digit = distance % 10
    distance = distance // 10
    
    if digit > 4:
        result += (digit - 1) * (9 ** i)
    else:
        result += digit * (9 ** i)
        
print(result)