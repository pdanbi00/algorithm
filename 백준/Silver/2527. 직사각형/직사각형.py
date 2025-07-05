def check(x1, y1, x2, y2, x3, y3, x4, y4):
    # 아예 안 만나는 경우
    # 첫번째 정사각형의 위쪽 꼭짓점 보다 두번째 정사각형의 아래쪽 꼭짓점이 높이 있는 경우
    if y2 < y3 or y4 < y1:
        return 'd'
    # 첫번째 정사각형의 아래쪽 꼭짓점 보다 두번째 정사각형의 위쪽 꼭짓점이 낮게 있는 경우
    elif y1 > y4 or y3 > y2:
        return 'd'
    # 첫번째 정사각형의 왼쪽 꼭짓점 보다 두번째 정사각형의 오른쪽 꼭짓점이 왼쪽에 있는 경우
    elif x1 > x4 or x3 > x2:
        return 'd'
    # 첫번째 정사각형의 오른쪽 꼭짓점 보다 두번째 정사각형의 왼쪽 꼭짓점이 오른쪽에 있는 경우
    elif x2 < x3 or x4 < x1:
        return 'd'


    # 한 점에서 만나는 경우 c
    # 첫번째 정사각형의 왼쪽 위 꼭짓점이 두번째 정사각형 오른쪽 아래 꼭짓점과 일치할 경우
    if (x1 == x4 and y2 == y3) or (x3 == x2 and y4 == y1):
        return 'c'
    # 첫번째 정사각형의 오른쪽 위 꼭짓점이 두번째 정사각형 왼쪽 아래 꼭짓점과 일치할 경우
    elif (x2 == x3 and y2 == y3) or (x4 == x1 and y4 == y1):
        return 'c'
    # 첫번째 정사각형의 왼쪽 아래 꼭짓점이 두번째 정사각형 오른쪽 위 꼭짓점과 일치할 경우
    elif (x1 == x4 and y1 == y4) or (x3 == x2 and y3 == y2):
        return 'c'
    # 첫번째 정사각형의 오른쪽 아래 꼭짓점이 두번째 정사각형 왼쪽 위 꼭짓점과 일치할 경우
    elif (x2 == x3 and y1 == y4) or (x4 == x1 and y3 == y2):
        return 'c'

    # 한 변에서 만나는 경우 b
    # 첫번째 정사각형의 위쪽 변이 두번째 정사각형의 아래쪽 변과 값이 같고 아래쪽 꼭짓점 중 하나가 y, q 사이에 있을 때
    if y2 == y3 and (x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4):
        return 'b'
    # 첫번째 정사각형의 아래쪽 변이 두번째 정사각형의 위쪽 변과 값이 같고 위쪽 꼭짓점 중 하나가 y, q 사이에 있을 때
    elif y1 == y4 and (x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4):
        return 'b'
    # 첫번째 정사각형의 왼쪽 변이 두번째 정사각형의 오른쪽 변과 값이 같고 오른쪽 꼭짓점 중 하나가 x, p 사이에 있을 때
    elif x1 == x4 and (y1 <= y4 <= y2 or y1 <= y3 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4):
        return 'b'
    # 첫번째 정사각형의 오른쪽 변이 두번째 정사각형의 왼쪽 변과 값이 같고 오른쪽 꼭짓점 중 하나가 x, p 사이에 있을 때
    elif x2 == x3 and (y1 <= y4 <= y2 or y1 <= y3 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4):
        return 'b'

    return 'a'


for _ in range(4):
    one_x1, one_y1, one_x2, one_y2, two_x1, two_y1, two_x2, two_y2 = map(int, input().split())
    print(check(one_x1, one_y1, one_x2, one_y2, two_x1, two_y1, two_x2, two_y2))