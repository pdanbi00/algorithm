N, K = map(int, input().split())

s = ['B'] * N

cnt = 0 # (A, B) 쌍의 개수
# 불가능한 경우 패스
max_cnt = 0 # 가장 많은 (A, B) 쌍의 개수
for i in range(N//2 + 1):
    max_cnt = max(max_cnt, i * (N-i))

# 만들 수 없는 경우
if max_cnt < K:
    print(-1)
    exit()

while cnt != K:
    idx = N-1 # 뒤에서부터 A 옮기기
    cnt -= s.count('A')
    s[idx] = 'A'
    while idx > 0 and s[idx-1] == 'B' and cnt != K:
        # A를 한 칸 앞으로 땡기기
        s[idx] = 'B'
        idx -= 1
        s[idx] = 'A'
        cnt += 1
print(''.join(s))