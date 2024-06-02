N, C = map(int, input().split())
messages = list(map(int, input().split()))

dict = {}
for i in range(N):
    if messages[i] in dict:
        dict[messages[i]][0] += 1
    else:
        dict[messages[i]] = [1, i]
arr = []
for k, v in dict.items():
    arr.append([k]+v)
arr.sort(key=lambda x: (x[1], -x[2]), reverse=True)
for a in arr:
    for i in range(a[1]):
        print(str(a[0]), end=' ')