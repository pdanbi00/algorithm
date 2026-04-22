def back_tracking(cnt):
    if cnt == K:
        nums.add(''.join(answer))
        return

    for k in cards:
        if cards[k]:
            answer.append(str(k))
            cards[k] -= 1
            back_tracking(cnt+1)
            answer.pop()
            cards[k] += 1

nums = set()
N = int(input())
K = int(input())
cards = dict()
answer = []
for _ in range(N):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

back_tracking(0)
print(len(nums))