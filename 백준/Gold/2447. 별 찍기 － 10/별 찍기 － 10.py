import sys
sys.setrecursionlimit(10**9)

def append_star(l):
    if l == 1:
        return ["*"]
    stars = append_star(l//3)
    L = []
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s + (" " * (l//3)) + s)
    for s in stars:
        L.append(s*3)
    return L

N = int(input())

print('\n'.join(append_star(N)))