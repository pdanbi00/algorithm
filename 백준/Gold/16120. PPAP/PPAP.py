stack = []
target = input()
ans = 'NP'
for i in target:
    stack.append(i)
    if len(stack) >= 4 and stack[-4:] == ["P", 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()
            
if len(stack) == 1 and stack[0] == 'P':
    ans = "PPAP"

print(ans)