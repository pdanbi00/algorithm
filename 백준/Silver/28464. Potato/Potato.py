from collections import deque
N = int(input())
potatoes = list(map(int, input().split()))

potatoes.sort(reverse=True)
potatoes = deque(potatoes)
park = 0
sang = 0

while potatoes:
    park += potatoes.popleft()
    if potatoes:
        sang += potatoes.pop()

print(sang, park)