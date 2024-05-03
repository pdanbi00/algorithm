# 이게 Union find라니...
# 현재 공항보다 작은 숫자의 공항 중에서 가장 오른쪽에 비어있는 칸을 루트로 union
def find(a):
    # 게이트가 자기 자신을 가리키는 경우 -> 게이트가 비어있따
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(root, a):
    root = find(root)
    a = find(a)

    if root == a:
        return
    parents[a] = root

Gate = int(input())
Plane = int(input())
parents = [i for i in range(Gate+1)]
ans = 0

for i in range(Plane):
    p = int(input())
    target = find(p)
    if target == 0:
        break
    union(target-1, target)
    ans += 1

print(ans)