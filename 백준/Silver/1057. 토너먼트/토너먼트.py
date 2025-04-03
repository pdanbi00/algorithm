N, J, H = map(int, input().split())
arr = [i for i in range(1, N+1)]
cnt = 1
while len(arr) >= 2:
    new_arr = []
    if len(arr) % 2 == 1:
        for i in range(0, len(arr)-1, 2):
            if arr[i] != J and arr[i] != H and arr[i+1] != J and arr[i+1] != H:
                new_arr.append(arr[i])
            elif (arr[i] == J and arr[i+1] == H) or (arr[i] == H and arr[i+1] == J):
                print(cnt)
                exit()
            elif arr[i] == J or arr[i] == H:
                new_arr.append(arr[i])
            elif arr[i+1] == J or arr[i+1] == H:
                new_arr.append(arr[i+1])
        new_arr.append(arr[-1])
    else:
        for i in range(0, len(arr), 2):
            if arr[i] != J and arr[i] != H and arr[i+1] != J and arr[i+1] != H:
                new_arr.append(arr[i])
            elif (arr[i] == J and arr[i+1] == H) or (arr[i] == H and arr[i+1] == J):
                print(cnt)
                exit()
            elif arr[i] == J or arr[i] == H:
                new_arr.append(arr[i])
            elif arr[i+1] == J or arr[i+1] == H:
                new_arr.append(arr[i+1])
    cnt += 1
    arr = new_arr

print(-1)