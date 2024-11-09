n = int(input())
cal = input() # 후위표기식
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

stack = []

for i in cal:
    if 'A' <= i <= 'Z':
        stack.append(nums[ord(i) - ord('A')])
    else: # 연산자 만나면
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
print('%.2f' %stack[0]) # 소수점 아래 2자리까지 제한
