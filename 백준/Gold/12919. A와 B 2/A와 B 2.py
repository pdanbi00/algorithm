S = input()
P = input()

answer = 0

def dfs(arr):
    global answer
    if arr == S:
        answer = 1
        return

    if len(arr) == 0:
        return
    
    if arr[-1] == 'A':
        dfs(arr[:-1])

    if arr[0] == 'B':
        dfs(arr[1:][::-1])

dfs(P)
print(answer)