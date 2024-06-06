N = int(input())
participants = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for p in participants:
    tmp = p - B
    if tmp > 0:
        if tmp % C != 0:
            ans += (tmp // C) + 1
        else:
            ans += tmp // C
print(ans)