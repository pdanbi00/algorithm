def solution(n, t, m, timetable):
    timetable.sort()
    crew_time = []
    for i in range(len(timetable)):
        crew_time.append(int(timetable[i][:2]) * 60 + int(timetable[i][3:]))
    bus_list = []
    # 도착 시간을 분으로 환산해서 생각
    time = 9 * 60

    # 버스 도착시간 배열
    for i in range(n):
        bus_list.append(time + t * i)
    idx = 0  # 다음 버스에 탈 크루의 인덱스
    for time in bus_list:
        cnt = 0  # 버스에 타는 크루 수
        # cnt < m : 버스 정원보다 타는 사람이 적은 경우 -> 버스에 자리가 남아있는 경우
        # idx < len(crew_time) : 탑승할 크루가 남아있다.
        # crew_time[i] <= time : 크루가 버스 도착 시간 전에 도착했다.
        while cnt < m and idx < len(crew_time) and crew_time[idx] <= time:
            idx += 1
            cnt += 1
        if cnt < m:  # 이 시간대에 탈 수 있는 사람 다 태우고 자리가 남았으면
            answer = time
        else:  # 사람 이미 다 찼으면 맨 마지막에 탄 사람보다 1분 빠르게
            answer = crew_time[idx - 1] - 1
    ans_h = answer // 60
    ans_m = answer % 60
    if ans_h <= 9:
        ans_h = '0' + str(ans_h)
    else:
        ans_h = str(ans_h)
    if ans_m <= 9:
        ans_m = '0' + str(ans_m)
    else:
        ans_m = str(ans_m)
    return ans_h + ':' + ans_m