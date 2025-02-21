K = int(input())
x = [2 ** i for i in range(21)] # 최소 K개의 초콜릿을 사기 위한 초콜릿

for i in x:
    if K <= i:
        choco = i
        break

cnt = 0 # 몇번 쪼개는지
temp = choco # 쪼갤 임시 초콜릿
if K != choco:
    while K:
        temp //= 2
        if K >= temp: # 원하는 사이즈보다 작을 경우
            K -= temp # 갉아먹기
            cnt += 1
        else: # 원하는 크기보다 쪼갠 크기가 클 경우
            cnt += 1 # 한번 더 쪼개기
print(choco, cnt)

