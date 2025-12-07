K = int(input())
tree = list(map(int, input().split()))

ans = [[] for _ in range(K)]

def binary_tree(array, depth):
    mid_idx = len(array) // 2

    if len(array) == 0:
        return

    binary_tree(array[:mid_idx], depth+1)
    ans[depth].append(array[mid_idx])
    binary_tree(array[mid_idx+1:], depth+1)

binary_tree(tree, 0)
for t in ans:
    print(*t)