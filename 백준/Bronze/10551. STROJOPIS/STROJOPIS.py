arr = input()

answer = [0] * 8
for i in range(len(arr)):
    if arr[i] in ['1', 'Q', 'A', 'Z']:
        answer[0] += 1
    elif arr[i] in ['2', 'W', 'S', 'X']:
        answer[1] += 1
    elif arr[i] in ['3', 'E', 'D', 'C']:
        answer[2] += 1
    elif arr[i] in ['4', 'R', 'F', 'V', '5', 'T', 'G', 'B']:
        answer[3] += 1
    elif arr[i] in ['6', 'Y', 'H', 'N', '7', 'U', 'J', 'M']:
        answer[4] += 1
    elif arr[i] in ['8', 'I', 'K', ',']:
        answer[5] += 1
    elif arr[i] in ['9', 'O', 'L', '.']:
        answer[6] += 1
    elif arr[i] in ['0', 'P', ';', '/', '-', '[', "'", ']', '=']:
        answer[7] += 1

for i in range(8):
    print(answer[i])