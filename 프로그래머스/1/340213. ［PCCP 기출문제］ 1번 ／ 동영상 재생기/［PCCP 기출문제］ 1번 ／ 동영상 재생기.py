def solution(video_len, pos, op_start, op_end, commands):
	# 주어진 문자열의 시간들을 ":"를 기준으로 나눔
    video_len = video_len.split(':');
    pos = pos.split(':');
    op_start = op_start.split(':');
    op_end = op_end.split(':');
    
    # 나눈 문자열은 ["mm", "ss"] 형태로 남아있기 때문에 int형으로 변경 후 분과 초를 합함
    len_sec = (int(video_len[0])*60) + int(video_len[1])
    pos_sec = (int(pos[0])*60) + int(pos[1])
    start_sec = (int(op_start[0])*60) + int(op_start[1])
    end_sec = (int(op_end[0])*60) + int(op_end[1])
    
    # commands를 순차적으로 돌며 명령 실행
    for i in commands:
		
        # 오프닝 스킵 기능
        if start_sec <= pos_sec <= end_sec:
            pos_sec = end_sec;
		
        # 넘기기 기능
        if i == 'next':
            if pos_sec >= len_sec-10:
                pos_sec = len_sec;
            else:
                pos_sec += 10;
        
        # 뒤로 가기 기능
        elif i == 'prev':
            if pos_sec <= 10:
                pos_sec = 0;
            else:
                pos_sec -= 10;
        
    # 오프닝 스킵 기능
    if start_sec <= pos_sec <= end_sec:
        pos_sec = end_sec;
	
    # 초를 다시 분:초 로 변경하기 위한 변수 생성
    mm = pos_sec // 60;
    ss = pos_sec % 60;
	
    # f-string 으로 int형을 string으로 변경(02는 1분 or 1초를 01로 표현하기 위함)
    answer = f'{mm:02}' + ':' + f'{ss:02}'
    return answer