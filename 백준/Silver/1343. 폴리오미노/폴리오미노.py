arr = list(input())
answer = ''
idx = 0
possible = True

while idx < len(arr):
    if arr[idx] == '.':
        answer += '.'
        idx += 1
    elif idx <= len(arr) - 4 and arr[idx] == 'X' and arr[idx+1] == 'X' and arr[idx+2] == 'X' and arr[idx+3] == 'X':
        answer += 'AAAA'
        idx += 4
    elif idx <= len(arr) - 2 and arr[idx] == 'X' and arr[idx+1] == 'X':
        answer += 'BB'
        idx += 2
    else:
        possible = False
        break

if possible:
    print(answer)
else:
    print("-1")