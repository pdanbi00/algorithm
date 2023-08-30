N = int(input())

list = map(int, input().split())
v = int(input())
count = 0
for num in list:
    if num == v:
        count += 1
print(count)