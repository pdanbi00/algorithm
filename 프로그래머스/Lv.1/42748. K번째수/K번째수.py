def solution(array, commands):
    answer = []
    for command in commands:
        n_arr = array[command[0]-1:command[1]]
        n_arr.sort()
        answer.append(n_arr[command[2]-1])
    return answer