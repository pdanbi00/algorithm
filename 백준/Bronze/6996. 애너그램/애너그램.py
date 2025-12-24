T = int(input())
for _ in range(T):
    a, b = input().split()
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if sorted_a == sorted_b:
        print(a + ' & ' + b + ' are anagrams.')
    else:
        print(a + ' & ' + b + ' are NOT anagrams.')