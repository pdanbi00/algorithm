line = input()
N = len(line)
if N == 1:
    print("AKARAKA")
else:
    akaraka = True

    def func(arr):
        if len(arr) == 1:
            return True
        N = len(arr)
        for i in range(N//2):
            if arr[i] != arr[N-1-i]:
                return False

        if N % 2 == 0:
            new_line_f = arr[:N//2]
            new_lien_b = arr[N//2:]
        else:
            new_line_f = arr[:N // 2]
            new_lien_b = arr[N // 2 + 1:]

        if func(new_line_f) and func(new_lien_b):
            return True
        return False

    akaraka = func(line)

    if akaraka:
        print("AKARAKA")
    else:
        print("IPSELENTI")