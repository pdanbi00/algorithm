import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (N+1)
child = [[] for _ in range(N+1)]
def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node, currentNode)

size = [0] * (N+1)
def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

makeTree(R, -1)
countSubtreeNodes(R)
for _ in range(Q):
    U = int(input())
    print(size[U])