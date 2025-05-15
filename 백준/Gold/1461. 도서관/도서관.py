N, M = map(int, input().split())
locations = list(map(int, input().split()))
ans = 0
idx = -1
locations.sort();
for i in range(N):
    if locations[i] > 0:
        idx = i
        break
if idx != -1:
    minus = locations[:idx]
    plus = locations[idx:]
else:
    minus = locations[:]
    plus = []

minus.sort()
plus.sort(reverse=True)

for i in range(0, len(minus), M):
    tmp = abs(min(minus[i:i+M]))
    ans += tmp * 2

for i in range(0, len(plus), M):
    tmp = abs(max(plus[i:i+M]))
    ans += tmp * 2
if len(minus) > 0 and len(plus) > 0 :
    ans -= max(abs(minus[0]), abs(plus[0]))
elif len(minus) > 0:
    ans -= abs(minus[0])
elif len(plus) > 0:
    ans -= abs(plus[0])

print(ans)