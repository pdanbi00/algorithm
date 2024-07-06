N, S, R = map(int, input().split())
damaged = set(map(int, input().split()))
more = set(map(int, input().split()))

answer = 0
intersection = damaged & more # 카약이 망가졌는데 하나 더 가져온 팀은 없애기
damaged = list(damaged - intersection)
more = list(more - intersection)

damaged.sort()
for i in damaged:
    if i - 1 in more: # 왼쪽 팀에게 카약 먼저 빌리기
        more.remove(i-1)
    elif i + 1 in more: # 오른쪽 팀한테 카약 먼저 빌리기
        more.remove(i+1)
    else:
        answer += 1
print(answer)