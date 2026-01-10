sign = {'-' : 0, "\\" : 1, '(' : 2, '@' : 3, '?' : 4, '>' : 5, '&' : 6, '%' : 7, '/' : -1}
while True:
    arr = input()
    if arr == '#':
        break

    n = len(arr)
    tmp = 0
    for i in range(n):
        num = sign[arr[i]]
        tmp += num * (8 ** (n-1-i))
        
    print(tmp)
