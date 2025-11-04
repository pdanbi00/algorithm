T = int(input())
for _ in range(T):
    land = []
    while True:
        price = int(input())
        if price == 0:
            break

        land.append(price)

    land.sort(reverse=True)
    tmp = 0
    possible = True
    for i in range(len(land)):
        tmp += (2 * (land[i] ** (i+1)))
        if tmp > 5000000:
            possible = False
            break

    if possible:
        print(tmp)
    else:
        print("Too expensive")