import sys
input = sys.stdin.readline

while True:
    try:
        X = int(input())
        X *= 10000000
        n = int(input())
        lego = []
        for _ in range(n):
            a = int(input())
            lego.append(a)
        lego.sort()

        start = 0
        end = n-1
        find = False
        while start < end:
            tmp = lego[start] + lego[end]
            if tmp == X:
                print('yes', lego[start], lego[end])
                find = True
                break

            elif tmp > X:
                end -= 1
            else:
                start += 1
        if not find:
            print('danger')

    except:
        break