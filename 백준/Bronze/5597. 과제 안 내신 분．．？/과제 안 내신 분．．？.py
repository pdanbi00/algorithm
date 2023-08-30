arr = list(range(1, 31))
for i in range(28):
    x = int(input())
    arr.remove(x)
print(min(arr))
print(max(arr))