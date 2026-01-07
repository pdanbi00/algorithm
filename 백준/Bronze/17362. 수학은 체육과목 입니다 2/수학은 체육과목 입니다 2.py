N = int(input())
tmp = (N-1) % 8

if tmp == 0:
    print(1)
elif tmp == 1 or tmp == 7:
    print(2)
elif tmp == 2 or tmp == 6:
    print(3)
elif tmp == 3 or tmp == 5:
    print(4)
else:
    print(5)