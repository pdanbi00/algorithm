N = int(input())
medicine = dict()
for _ in range(N):
    power, name = map(int, input().split())
    medicine[power] = name

R = int(input())
for _ in range(R):
    symptoms = list(map(int, input().split()))
    k = symptoms[0]
    # print(k)
    tmp = []
    possible = True
    for i in range(1, k+1):
        # print(symptoms[i])
        if symptoms[i] in medicine:
            tmp.append(medicine[symptoms[i]])
        else:
            possible = False
            break
    if possible:
        print(*tmp)
    else:
        print("YOU DIED")