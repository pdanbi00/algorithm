N, K = map(int, input().split())
belt = list(map(int, input().split()))
boxes = [False] * (2*N)
ans = 1
zero = 0
while True:
    temp1 = belt[2*N-1]
    temp2 = boxes[2*N-1]
    for i in range(2*N-1, 0, -1):
        belt[i] = belt[i-1]
        boxes[i] = boxes[i-1]
    belt[0] = temp1
    boxes[0] = temp2
    if boxes[N-1]:
        boxes[N-1] = False

    for i in range(N-2, -1, -1):
        if boxes[i]:
            if boxes[i+1] == False and belt[i+1] >= 1:
                boxes[i+1] = True
                boxes[i] = False
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    zero += 1
    if boxes[N-1]:
        boxes[N-1] = False

    if belt[0] > 0:
        boxes[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zero += 1

    if zero >= K:
        print(ans)
        break
    ans += 1
