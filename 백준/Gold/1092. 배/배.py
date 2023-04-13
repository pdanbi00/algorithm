# import sys
# input = sys.stdin.readline

N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)
cnt = 0
if box[0] > crain[0]:
    cnt = -1
else:
    while box:
        for c in crain:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break

        cnt += 1
print(cnt)