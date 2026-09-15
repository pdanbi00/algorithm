def solution(my_string):
    arr = my_string.split(" ")
    answer = int(arr[0])
    idx = 0
    N = len(arr)
    
    while idx < N:
        if (arr[idx] == "+"):
            answer += int(arr[idx+1])
        elif (arr[idx] == "-"):
            answer -= int(arr[idx+1])
        idx += 1
    return answer