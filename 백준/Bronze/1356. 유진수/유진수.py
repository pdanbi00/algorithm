N = input()
l = len(N)
possible = False
for i in range(1, l):
    n1 = 1
    for j in range(i):
        n1 *= int(N[j])
    n2 = 1
    for j in range(i, l):
        n2 *= int(N[j])
    if n1 == n2:
        possible = True
        break
    # print(n1, n2)
if possible:
    print("YES")
else:
    print("NO")