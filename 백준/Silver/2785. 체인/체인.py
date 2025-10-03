N = int(input())
chains = list(map(int, input().split()))

chains.sort()

idx = 0 # 해체할 체인의 인덱스
right = N-1 # 해체해서 오른쪽에서 몇번째 고리까지 연결시켰는지
cnt = 0
# 해체한 고리 개수가 앞으로 필요한 고리 개수보다 많으면 break
while True:
    if right - chains[idx] > idx:
        cnt += chains[idx]
        right -= chains[idx]
        idx += 1
    else:
        cnt += right - idx
        break

print(cnt)