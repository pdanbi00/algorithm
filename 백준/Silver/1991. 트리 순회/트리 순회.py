# 딕셔너리로 하면 문자 숫자로 변환하고 이거 안해도 됨~~
N = int(input())
dict = {}
for i in range(N):
    node, left, right = input().split()
    dict[node] = [left, right]

# 전위순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(dict[root][0])
        preorder(dict[root][1])

# 중위순회
def inorder(root):
    if root != '.':
        inorder(dict[root][0])
        print(root, end='')
        inorder(dict[root][1])

# 후위순회
def postorder(root):
    if root != '.':
        postorder(dict[root][0])
        postorder(dict[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')