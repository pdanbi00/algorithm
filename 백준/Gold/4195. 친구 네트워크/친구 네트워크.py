import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

# 문자열이라서 부모 대소 비교가 안되니깐 무조건 a가 부모라고 생각하기
def union(a, b):
    # 각 부모노드 찾기
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        count[a] += count[b]
    print(count[a])

T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    count = {}
    for i in range(F):
        f1, f2 = input().split()
        # 친구 관계의 없는 친구면 추가
        if f1 not in parents:
            parents[f1] = f1
            count[f1] = 1

        if f2 not in parents:
            parents[f2] = f2
            count[f2] = 1

        union(f1, f2)
