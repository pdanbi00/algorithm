def solution(s):
    answer = 0
    N = len(s)
    for i in range(N):
        tmp = s[i:] + s[:i]
        stack = []
        possible = True
        for i in range(N):
            if tmp[i] == '{' or tmp[i] == '(' or tmp[i] == '[':
                stack.append(tmp[i])
            elif tmp[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    possible = False
                    break
            elif tmp[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    possible = False
                    break
            elif tmp[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    possible = False
                    break
                    
        if possible and not stack:
            answer += 1
    return answer