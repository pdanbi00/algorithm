def solution(sizes):
    w = []
    h = []
    for size in sizes:
        if size[0] >= size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            h.append(size[0])
            w.append(size[1])
    return max(h) * max(w)