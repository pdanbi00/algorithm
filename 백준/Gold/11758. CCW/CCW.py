dots = []
for _ in range(3):
    x, y = map(int, input().split())
    dots.append((x, y))
find = False
dx1 = dots[1][0] - dots[0][0]
dy1 = dots[1][1] - dots[0][1]

if dots[0][0] != dots[1][0]:
    a = dy1 / dx1 # 기울기 찾기
    # 첫번째 두번째 점 기준으로 y = ax + b 식 구하기
    b = dots[0][1] - a * dots[0][0]

    # 두번째 점, 세번째 점으로 기울기 구하기
    dx2 = dots[2][0] - dots[1][0]
    dy2 = dots[2][1] - dots[1][1]
    degree = dy2 / dx2
    if a == degree: # 일직선인 경우
        answer = 0
        find = True

    if not find:
        tmp = a * dots[2][0] + b
        if dots[0][0] < dots[1][0]:
            if dots[2][1] < tmp:
                answer = -1
            else:
                answer = 1
        else:
            if dots[2][1] < tmp:
                answer = 1
            else:
                answer = -1

else:
    if dots[0][1] > dots[1][1]:
        if dots[2][0] > dots[0][0]:
            answer = 1
        elif dots[2][0] == dots[0][0]:
            answer = 0
        else:
            answer = -1
    else:
        if dots[2][0] > dots[0][0]:
            answer = -1
        elif dots[2][0] == dots[0][0]:
            answer = 0
        else:
            answer = 1

print(answer)