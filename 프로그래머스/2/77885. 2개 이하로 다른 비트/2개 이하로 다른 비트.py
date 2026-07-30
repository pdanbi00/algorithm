def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        num = numbers[i]
        if (num % 2 == 0):
            answer.append(num+1)
            continue
        else:
            tmp = (~num) & (num+1)
            target = num + (tmp>>1)
            answer.append(target)
    return answer