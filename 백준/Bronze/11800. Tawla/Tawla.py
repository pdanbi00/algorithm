T = int(input())

info = {1:"Yakk", 2:"Doh", 3:"Seh", 4:"Ghar", 5:"Bang", 6:"Sheesh"}
for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a == b:
        if a == 1:
            print(f"Case {tc}: Habb Yakk")
        elif a == 2:
            print(f"Case {tc}: Dobara")
        elif a == 3:
            print(f"Case {tc}: Dousa")
        elif a == 4:
            print(f"Case {tc}: Dorgy")
        elif a == 5:
            print(f"Case {tc}: Dabash")
        elif a == 6:
            print(f"Case {tc}: Dosh")
    else:
        if max(a, b) == 6 and min(a, b) == 5:
            print(f"Case {tc}: Sheesh Beesh")
        else:
            print(f"Case {tc}: {info[max(a, b)]} {info[min(a, b)]}")