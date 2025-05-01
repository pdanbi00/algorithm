N, C = map(int, input().split())
M = int(input())
boxes = []

for _ in range(M):
    a, b, c = map(int, input().split())
    boxes.append((a, b, c))

boxes.sort(key=lambda x : x[1])

village = [C] * (N+1) # 각 마을에서 싣을 수 있는 택배의 개수
ans = 0
for s, e, c in boxes:
    tmp = C
    for i in range(s, e): # 출발지부터 도착지까지
        tmp = min(tmp, village[i]) # 옮길 수 있는 것과 상한선 중 작은 값
    tmp = min(tmp, c) # 옮길 수 있는 상자 개수랑 실제 박스 개수
    for k in range(s, e):
        village[k] -= tmp
    ans += tmp
print(ans)
