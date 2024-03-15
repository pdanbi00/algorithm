N = int(input())
front = []
middle = []
last = []
graph = [[-1]*2 for _ in range(N)]

for i in range(N):
    node, left, right = input().split()
    if left != '.':
        graph[ord(node)-65][0] = ord(left)-65
    if right != '.':
        graph[ord(node)-65][1] = ord(right)-65

# 전위순회
def f(idx):
    front.append(idx)
    if graph[idx][0] > -1:
        f(graph[idx][0])
    if graph[idx][1] > -1:
        f(graph[idx][1])

# 중위순회
def m(idx):
    if graph[idx][0] > -1:
        m(graph[idx][0])
    middle.append(idx)
    if graph[idx][1] > -1:
        m(graph[idx][1])

# 후위순회
def l(idx):
    if graph[idx][0] > -1:
        l(graph[idx][0])
    if graph[idx][1] > -1:
        l(graph[idx][1])
    last.append(idx)
f(0)
m(0)
l(0)
for i in range(len(front)):
    c = front[i]
    print(chr(c+65), end='')
print()
for i in range(len(middle)):
    c = middle[i]
    print(chr(c+65), end='')
print()
for i in range(len(last)):
    c = last[i]
    print(chr(c+65), end='')
print()