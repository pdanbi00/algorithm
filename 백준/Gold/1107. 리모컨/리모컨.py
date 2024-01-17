broken = [False] * 10

N = int(input()) # 최종적으로 이동하려는 채널 번호
M = int(input()) # 고장난 버튼 개수
if M > 0:
    broke = list(map(int, input().split()))
else:
    broke = []
for num in broke:
    broken[num] = True

def possible(num):
    if num == 0:
        if broken[0]:
            return 0
        else:
            return 1
    length = 0
    while num > 0:
        if broken[num % 10] == False:
            num = num // 10
            length += 1
        else:
            return 0
    return length

ans = abs(N-100) # 정답 초기값
for i in range(1000001):
    l = possible(i)
    if l > 0:
        press = abs(N-i)
        if ans > l + press:
            ans = l + press
print(ans)