def solution(sizes):
    answer = 0
    width = [] # 가로 세로 중 긴 길이
    length = [] # 가로 세로 중 짧은 길이
    for size in sizes:
        if size[0] > size[1]:
            width.append(size[0])
            length.append(size[1])
        else:
            width.append(size[1])
            length.append(size[0])
    return max(width) * max(length)