def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    start = 0
    end = distance
    answer = 0
    while start <= end:
        mid = (start+end) // 2
        pre_rock = 0
        delete_rock = 0
        for rock in rocks:
            dist = rock - pre_rock
            if dist < mid:
                delete_rock += 1
            else:
                pre_rock = rock
                
        if delete_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer