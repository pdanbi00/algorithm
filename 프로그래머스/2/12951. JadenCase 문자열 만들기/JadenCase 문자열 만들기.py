def solution(s):
    answer = ''
    arr = s.split(" ")
    for i in range(len(arr)):
        tmp = arr[i][:1].upper() + arr[i][1:].lower()
        if i != len(arr)-1:
            answer += tmp + " "
        else:
            answer += tmp
    return answer