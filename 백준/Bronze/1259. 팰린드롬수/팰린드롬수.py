while True:
    arr = input()
    if arr == '0':
        break
    new_list = [0]*len(arr)
    for i in range(len(arr)):
        new_list[i] = arr[len(arr)-1-i]
    new_list = "".join(new_list)
    if arr == new_list:
        print('yes')
    else:
        print('no')
