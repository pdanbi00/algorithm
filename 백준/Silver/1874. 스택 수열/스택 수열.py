N = int(input())
stack = []
ans = []
no_ans = False
now = 1
for i in range(N):
    num = int(input())
    # num까지 숫자 스택에 넣기
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    # num이랑 스택 제일 위 숫자가 같으면 제거
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    
    else:
    # stack의 제일 위 숫자가 입력받은 수가 아니면 스택을 만들 수 없음
    # 12345 이렇게 오름차순으로 스택이 입력되는데
    # 제일 위에 수가 입력받은 숫자보다 크면 입력받은 수는 TOP보다 밑에 쌓여있음.
    # 그러면 그 수를 찾을때까지 pop 계속하면 수열이 달라짐
        print("NO")
        no_ans = True
        break
if not no_ans:
    for i in ans:
        print(i)
