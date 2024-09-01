while True:
    lines = list(map(int, input().split()))
    if lines == [0, 0, 0]:
        break
    lines.sort()
    if lines[2] >= lines[0] + lines[1]:
        print("Invalid")
    else:
        if lines[0] == lines[1] and lines[1] == lines[2]:
            print("Equilateral")
        elif lines[0] == lines[1] or lines[0] == [2] or lines[1] == lines[2]:
            print("Isosceles")
        else:
            print("Scalene")