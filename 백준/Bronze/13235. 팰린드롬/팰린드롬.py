arr = input()
N = len(arr)

possible = True

for i in range(N//2):
    if arr[i] != arr[N-1-i]:
        possible = False
        break

if possible:
    print("true")
else:
    print("false")