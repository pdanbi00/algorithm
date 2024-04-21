N, M = map(int ,input().split())
girl_group = {}
girl_name = {}
for i in range(N):
    group_name = input()
    count = int(input())
    members = [input() for _ in range(count)]
    members.sort()
    girl_group[group_name] = members
    for m in members:
        girl_name[m] = group_name
for i in range(M):
    name = input()
    kind = int(input())
    if kind == 0:
        for m in girl_group[name]:
            print(m)
    else:
        print(girl_name[name])
