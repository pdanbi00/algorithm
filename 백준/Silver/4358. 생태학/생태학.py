import sys
input = sys.stdin.readline
names = set()
name_dict = dict()
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    cnt += 1
    names.add(tree)
    if tree in name_dict:
        name_dict[tree] += 1
    else:
        name_dict[tree] = 1

names = list(names)
names.sort()
for n in names:
    tmp = round((name_dict[n] / cnt) * 100, 4)
    print("%s %.4f" %(n, tmp))