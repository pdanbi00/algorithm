line = input()
N = len(line)
def func(arr):
    if len(arr) == 1:
        return True
    
    N = len(arr)
    
    prefix = arr[:N//2]
    if N % 2 == 0:
        suffix = arr[N//2:]
    else:
        suffix = arr[N//2+1:]
    
    if arr == arr[::-1] and prefix == prefix[::-1] and suffix == suffix[::-1]:
        return func(prefix) and func(suffix)
    return False

if func(line):
    print("AKARAKA")
else:
    print("IPSELENTI")