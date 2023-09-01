tc = int(input())

for _ in range(tc):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if N % H == 0:
        room = N // H
        floor = H
    print(floor * 100 + room)