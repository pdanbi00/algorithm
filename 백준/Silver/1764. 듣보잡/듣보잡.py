import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_list = {}
ans_name = []
for i in range(N):
    name = input().strip()
    name_list[name] = 1
for i in range(M):
    name = input().strip()
    if name in name_list:
        ans_name.append(name)
ans_name.sort()
print(len(ans_name))
for n in ans_name:
    print(n)
