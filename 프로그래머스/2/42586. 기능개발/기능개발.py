def solution(progresses, speeds):
    answer = []
    time = []
    for i in range(len(progresses)):
        tmp = 100 - progresses[i]
        if tmp % speeds[i] == 0:
            time.append(tmp // speeds[i])
        else:
            time.append(tmp // speeds[i] + 1)
    i = 0
    while i < len(time):
        tmp = time[i]
        cnt = 0
        for j in range(i, len(time)):
            if time[j] > tmp:
                break
            elif time[j] <= tmp:
                cnt += 1
                i += 1
        answer.append(cnt)
    return answer