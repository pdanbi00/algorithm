def func(start, end, level):
    if start == end:
        ans[level].append(tree[start])
        return

    center = (start + end) // 2
    func(start, center - 1, level + 1)
    ans[level].append(tree[center])
    func(center+1, end, level+1)

K = int(input())
tree = list(map(int, input().split()))
l = len(tree)

ans = [[] for _ in range(K)]

func(0, l-1, 0)
for t in ans:
    print(*t)

