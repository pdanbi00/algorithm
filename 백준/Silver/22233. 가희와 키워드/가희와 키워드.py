import sys
input = sys.stdin.readline
N, M = map(int, input().split())
kewords = set([input().strip() for _ in range(N)])

for _ in range(M):
    key_set = set(input().strip().split(','))
    kewords -= key_set
    print(len(kewords))