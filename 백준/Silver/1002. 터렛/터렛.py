from math import sqrt
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0: # 두 원의 중심이 같은 경우
        if r1 == r2: # 두 원의 크기가 같은 경우
            print(-1)
        else:# 한 원 안에 다른 원이 들어가 있는 경우
            print(0)
    else: #두 원의 중심이 다른 경우
        if abs(r1-r2) == distance or (r1+r2) == distance: # 앞에꺼는 한 원이 다른 원에 내접하는경우. 뒤에꺼는 두 원이 외접으로 한점에서 만나는 경우
            print(1)
        elif abs(r1-r2) < distance and distance < (r1+r2): # 두 원이 두 점에서 만나는 경우
            print(2)
        else:
            print(0)

