N = int(input())
potatoes = list(map(int, input().split()))

potatoes.sort(reverse=True)

park = 0
sang = 0
s = 0
e = N-1

while s <= e:
    park += potatoes[s]
    if s < e:
        sang += potatoes[e]

    s += 1
    e -= 1

print(sang, park)