import sys
sys.setrecursionlimit(10**6)

s = input()
order = [""] * (len(s))

def func(arr, start_idx):
    if arr == "":
        return

    char = min(arr)
    idx = arr.index(char)

    order[start_idx + idx] = char

    print("".join(order))

    func(arr[idx+1:], start_idx+idx+1)
    func(arr[:idx], start_idx)

func(s, 0)