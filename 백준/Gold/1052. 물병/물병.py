N, K = map(int, input().split())
cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1') # 1이 오른쪽에서 몇번째에 있는지 찾기
    cnt += 2**idx
    N += 2 ** idx

print(cnt)