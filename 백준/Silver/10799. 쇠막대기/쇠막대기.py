# 여는 괄호일 경우는 stack에 넣기
# 레이저가 나오면 스택에 쌓인 괄호만큼 개수 더하기
# 그냥 닫는 괄호일 경우 개수에 1 추가하고 스택에서 pop 해주기

line = input()
stack = []
cnt= 0
for i in range(len(line)):
    if line[i] == "(":
        stack.append("(")
    else:
        if line[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)