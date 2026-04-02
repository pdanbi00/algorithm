N = input().rstrip()
l = len(N)

if l == 1:
    print("NO")
else:
    n1, n2 = 1, 1
    
    for i in range(l-1):
        n1 *= int(N[i])
    
    n2 = int(N[l-1])
    if n1 == n2:
        print("YES")
    else:
        possible = False
        for i in range(l-2, 0, -1):
            if int(N[i]) == 0:
                n1, n2 = 1, 1
                for j in range(i):
                    n1 *= int(N[j])
                for j in range(i, l):
                    n2 *= int(N[j])
            else:
                n2 *= int(N[i])
                n1 //= int(N[i])
    
            if n1 == n2:
                possible = True
                break
        if possible:
            print("YES")
        else:
            print("NO")