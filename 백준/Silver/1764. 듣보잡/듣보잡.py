# 교집합 만들어서 풀기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    name = input().strip()
    a.append(name)
for i in range(M):
    name = input().strip()
    b.append(name)

answer = list(set(a) & set(b))
answer.sort()
print(len(answer))
for n in answer:
    print(n)
