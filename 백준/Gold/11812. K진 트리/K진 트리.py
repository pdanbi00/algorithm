import sys
input = sys.stdin.readline
N, K, Q = map(int, input().split())

# 부모 노드로 이동
def find(x):
    return (x-2) // K + 1

def union(a, b):
    distance = 0
    while a != b:
        if a > b:
            a = find(a)
        else:
            b = find(b)
        distance += 1
    return distance

for _ in range(Q):
    a, b = map(int, input().split())
    if K == 1:
        print(abs(a-b))
    else:
        print(union(a, b))
