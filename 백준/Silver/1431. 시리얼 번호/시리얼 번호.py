N = int(input())
guitars = []
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(N):
    guitar = input()
    total = 0
    for j in range(len(guitar)):
        if guitar[j] in nums:
            total += int(guitar[j])
    guitars.append((guitar, len(guitar), total))
guitars.sort()
guitars.sort(key=lambda x : (x[1], x[2]))
for g in guitars:
    print(g[0])