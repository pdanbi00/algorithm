def isAvailableSrt(str):
    todo = list(str)

    while len(todo) >= 3:
        # 종이 접어서 보면 방향이 같고 같고 반대, 같고 같고 반대 이럼
        for i in range(2, len(todo), 2):
            if todo[i-2] == todo[i]:
                return False
        nextTodo = []
        for i in range(1, len(todo), 2):
            nextTodo.append(todo[i])
        todo = nextTodo
    return True

T = int(input())
for _ in range(T):
    curinput = str(input())

    if isAvailableSrt(curinput):
        print('YES')
    else:
        print('NO')