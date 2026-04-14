N = int(input())
names = [input() for _ in range(N)]

asc = sorted(names)
desc = sorted(names, reverse=True)
if names == asc:
    print("INCREASING")
elif names == desc:
    print("DECREASING")
else:
    print("NEITHER")