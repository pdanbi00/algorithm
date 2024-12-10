# DFS
# 현재까지 결과를 파라미터에 담고 그 다음 계산을 진행하는데
# 다음에 오는 수가 괄호에 속해있거나 속해있지 않다고 가정

N = int(input())
calc = list(input())
answer = -1 * (2 ** 31)
def calculate(a, op, b):
    if op == '+':
        num = a + b
    elif op == '*':
        num = a * b
    elif op == '-':
        num = a - b
    return num


# 1 + 2 + 3 - 4 - 5 일때 1 + 2까지 하면 현재 값은 3임
# 다음 연산은 3 + 3 - 4 - 5
#      아니면 3 + (3 - 4) - 5
# 괄호는 2개의 숫자와 1개의 연산자를 포함하고, 괄호 안에 괄호는 불가능하기 때문에
# 3 + (3 - 4) - 5에는 괄호를 더이상 추가 할 수 없음

def dfs(idx, value):
    global answer
    if idx == N-1:
        answer = max(answer, value)
        return
    if idx + 2 < N:
        # a + b + c + d + ... 에서 a + b로 계산 (idx 다음에 나오는 수가 괄호에 포함 안 되어있다고 가정)
        # 다음에 나오는 수랑 계산하는데 다음에 나오는 수가 괄호 안 쳐져 있음
        next_value = calculate(value, calc[idx+1], int(calc[idx+2]))
        dfs(idx+2, next_value)

    if idx + 4 < N:
        # a + b + c + d + ... 에서 a + (b + c)로 계산 (idx 다음에 나오는 수가 괄호에 포함 되어있다고 가정)
        # 다음에 나오는 수랑 계산하는데 다음에 나오는 수가 그 다음 수랑 괄호가 쳐져있을때
        next_next_value = calculate(int(calc[idx+2]), calc[idx+3], int(calc[idx+4]))
        next_value = calculate(value, calc[idx+1], next_next_value)
        dfs(idx+4, next_value)

dfs(0, int(calc[0]))
print(answer)
