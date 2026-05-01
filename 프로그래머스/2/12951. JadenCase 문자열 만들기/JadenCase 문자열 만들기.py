def solution(s):
    arr = s.split(" ")
    for i in range(len(arr)):
        arr[i] = arr[i][:1].upper() + arr[i][1:].lower()
    answer = ' '.join(arr)
    return answer