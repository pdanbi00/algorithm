import sys
input = sys.stdin.readline
N = int(input())
list = []
for i in range(N):
    line = input().split()
    if line[0] == "push":
        list.append(line[1])
    elif line[0] == "pop":
        if len(list) == 0:
            print("-1")
        else:
            print(list.pop())
    elif line[0] == "size":
        print(len(list))
    elif line[0] == "empty":
        if len(list) == 0:
            print("1")
        else:
            print("0")
    elif line[0] == "top":
        if len(list) == 0:
            print("-1")
        else:
            print(list[len(list)-1])