def solution(fees, records):
    answer = []
    total_info = dict()
    cur_info = dict()
    for record in records:
        time, car, come = record.split()
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
        
        if come == "OUT":
            if car in total_info:
                total_info[car] += time - cur_info[car]
            else:
                total_info[car] = time - cur_info[car]
            cur_info.pop(car)
        else:
            cur_info[car] = time
            
    if cur_info:
        for cur in cur_info.keys():
            if cur in total_info:
                total_info[cur] += (23 * 60 + 59) - cur_info[cur]
            else:
                total_info[cur] = (23 * 60 + 59) - cur_info[cur]
    cars = sorted(list(total_info.keys()))

    for c in cars:
        tmp = fees[1]
        if total_info[c] > fees[0]:
            total_info[c] -= fees[0]
            if total_info[c] % fees[2]:
                tmp += (total_info[c] // fees[2] + 1) * fees[3]
            else:
                tmp += (total_info[c] // fees[2]) * fees[3]
        answer.append(tmp)
    return answer