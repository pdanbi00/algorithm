from math import sqrt
from collections import deque

N = int(input())
arr = list(map(int, input().split()))
answer = dict()
cards = []

maxNum = 0 # 입력받은 숫자 중 최댓값

for i in range(N):
    maxNum = max(arr[i], maxNum)
    cards.append((i, arr[i]))
    answer[arr[i]] = 0

# 입력받은 수를 오름차순으로 정렬
cards.sort(key=lambda x : x[1])

for i in range(N):
    idx, num = cards[i]

    # 에라토스테네스의 체랑 비슷하게
    # target은 num의 배수
    for target in range(num * 2, maxNum+1, num):
        # target이 cards에 등장한 값이라면 비교
        # 근데 target이 num의 배수 이기 때문에 항상 target이 이김
        if target in answer:
            answer[num] += 1
            answer[target] -= 1

for k, v in answer.items():
    print(v, end=" ")