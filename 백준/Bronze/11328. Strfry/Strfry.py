N = int(input())
for _ in range(N):
    arr1, arr2 = input().split()
    dict1 = {}
    ans = True
    for i in range(len(arr1)):
        if arr1[i] in dict1:
            dict1[arr1[i]] += 1
        else:
            dict1[arr1[i]] = 1
    for j in arr2:
        if j in dict1:
            dict1[j] -= 1
        else:
            ans = False
            break
    if ans:
        for key, value in dict1.items():
            if value != 0:
                ans = False
                break
        if not ans:
            print('Impossible')
        else:
            print('Possible')
    else:
        print('Impossible')