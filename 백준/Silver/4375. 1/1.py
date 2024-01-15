while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    count = 1
    while True:
        num = num * 10 + 1
        num = num % n
        if num == 0:
            print(count)
            break
        else:
            count += 1
        