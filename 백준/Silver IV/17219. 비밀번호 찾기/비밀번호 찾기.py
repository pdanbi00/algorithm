import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
for i in range(N):
    site, password = input().split()
    dict[site] = password
for i in range(M):
    site = input().rstrip()
    print(dict[site])