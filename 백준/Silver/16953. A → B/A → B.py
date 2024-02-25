A, B = map(int, input().split())
ans = 1
while B != A:
    temp = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    ans += 1
    if temp == B: # 값의 변화가 없으면 무한루프에 빠진거니깐 출력하고 나오기
        print(-1)
        break
else:
    print(ans)