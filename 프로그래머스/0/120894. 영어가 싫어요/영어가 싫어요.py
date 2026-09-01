def solution(numbers):
    answer = 0
    idx = 0
    N = len(numbers)
    while idx < N:
        answer *= 10
        if idx + 3 < N:
            tmp = numbers[idx:idx+4]
            if ''.join(tmp) == 'zero':
                answer += 0
                idx += 4
                continue
            elif ''.join(tmp) == 'four':
                answer += 4
                idx += 4
                continue
            elif ''.join(tmp) == 'five':
                answer += 5
                idx += 4
                continue
            elif ''.join(tmp) == 'nine':
                answer += 9
                idx += 4
                continue

        if idx + 2 < N:
            tmp = numbers[idx:idx+3]
            if ''.join(tmp) == 'one':
                answer += 1
                idx += 3
                continue
            elif ''.join(tmp) == 'two':
                answer += 2
                idx += 3
                continue
            elif ''.join(tmp) == 'six':
                answer += 6
                idx += 3
                continue
        if idx + 4 < N:
            tmp = numbers[idx:idx+5]
            if ''.join(tmp) == 'three':
                answer += 3
                idx += 5
                continue
            elif ''.join(tmp) == 'seven':
                answer += 7
                idx += 5
                continue
            elif ''.join(tmp) == 'eight':
                answer += 8
                idx += 5
                continue
            
        print(tmp)
    return answer