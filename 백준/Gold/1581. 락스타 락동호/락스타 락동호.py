FF, FS, SF, SS = map(int, input().split())

ans = 0
# FF가 있으면 먼저 다 싣기
ans += FF
# 느리게 시작하는 곡으로 넘어가서 SS 다 넣기
if FS > 0:
    ans += SS
    if FS > SF:
        ans += SF * 2 + 1
    else:
        ans += FS * 2

# 빠르게 시작하는 곳이 없다면
if FF == 0 and FS == 0:
    ans += SS
    if SF > 0:
        ans += 1

print(ans)