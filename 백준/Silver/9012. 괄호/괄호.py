T = int(input())
for _ in range(T):
    line = input()
    stack = []
    possible = True
    for l in line:
        if l == '(':
            stack.append(l)
        elif l == ')':
            if stack:
                stack.pop()
            else:
                possible = False
                break
    if stack:
        print("NO")
    elif not possible:
        print("NO")
    else:
        print("YES")