# 문제만 보고 버블정렬 쓰면 시간초과난다 속지마라
# def bubble(arr):
#     global ans
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[j]
#                 ans += 1
#                 if arr == arr2:
#                     return
#
# 병합정렬로 접근해야 됨
def merge(arr, s, mid, e):
    global ans
    merge_list = []
    i = s
    j = mid + 1
    while i <= mid and j <= e:
        if arr[i]<= arr[j]:
            merge_list.append(arr[i])
            i += 1
        else:
            merge_list.append(arr[j])
            j += 1
            ans += (mid + 1 - i)
    while i <= mid:
        merge_list.append(arr[i])
        i += 1


    while j <= e:
        merge_list.append(arr[j])
        j += 1
        ans += (mid + 1 - i)
    x = 0
    for k in range(s, e+1):
        arr[k] = merge_list[x]
        x += 1


def mergesort(arr, s, e):
    if s==e:
        return
    mid = (s+e) // 2
    mergesort(arr, s, mid) # 왼쪽정렬
    mergesort(arr, mid+1, e) # 오른쪽 정렬 이거는 인덱스가 아니기 때문에 mid+1 해야 안겹침
    merge(arr, s, mid, e)

N = int(input())
arr = list(map(int, input().split()))
ans = 0
mergesort(arr, 0, len(arr)-1)
print(ans)