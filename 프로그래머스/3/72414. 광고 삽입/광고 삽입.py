def solution(play_time, adv_time, logs):
    start_time = []
    end_time = []
    time = {}
    playtime = int(play_time[0:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:8])
    advtime = int(adv_time[0:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:8])
    # 초 단위로 변환해서 계산
    for i in range(len(logs)):
        s, e = logs[i].split("-")
        s_time = int(s[0:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8])
        e_time = int(e[0:2]) * 3600 + int(e[3:5]) * 60 + int(e[6:8])
        start_time.append(s_time)
        end_time.append(e_time)
    dp = [0] * 36000000
    # dp[x] : x 시간에 시작된 재생 구간 수 - x 시간에 끝난 재생 구간 수
    # 즉, 구간별 시청자 수 계산
    for i in range(len(logs)):
        dp[start_time[i]] += 1
        dp[end_time[i]] -= 1
        
    # dp[x] : x시간을 포함하는 재생 구간 수
    for i in range(1, playtime+1):
        dp[i] = dp[i] + dp[i-1]
    # 누적합 구하기.
    # dp[x] : 0초부터 x+1초까지의 구간을 포함하는 누적 재생시간
    for i in range(1, playtime+1):
        dp[i] = dp[i] + dp[i-1]
    max_view = dp[advtime]
    max_time = 0
    # 누적 재생시간이 가장 긴 구간 구하기
    for i in range(1, playtime+1-advtime):
        view = dp[i+advtime-1] - dp[i-1]
        if view > max_view:
            max_view = view
            max_time = i
    h = max_time//3600
    m = (max_time % 3600) // 60
    s = (max_time % 3600) % 60
    if h < 10:
        h = '0'+str(h)
    if m < 10:
        m = '0'+str(m)
    if s < 10:
        s = '0'+str(s)
    return str(h)+':'+str(m)+':'+str(s)