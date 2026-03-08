def check(num):
    l = len(num)
    for i in range(l//2):
        if num[i] != num[l-1-i]:
            return False
    # print(num)
    return True


while True:
    N = input()
    n = int(N)
    zero = 0
    l = len(str(n))
    for i in range(len(N)):
        if N[i] == '0':
            zero += 1
        else:
            break


    if N == '0':
        break

    for i in range(1000000000):
        if len(str(n + i)) > l:
            zero -= 1
            l += 1
        num = '0' * zero + str(n+i)
        if check(num):
            print(i)
            break


'''
000121
00000
0
'''