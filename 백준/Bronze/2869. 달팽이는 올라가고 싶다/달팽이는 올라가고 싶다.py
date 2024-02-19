from math import ceil
A, B, V = map(int, input().split())
height = V - A
ans= ceil(height/(A-B)) + 1
print(ans)
