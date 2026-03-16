A, B = input().split()

tmp_A = 0
tmp_B = 0
for i in A:
    tmp_A += int(i)

for i in B:
    tmp_B += int(i)

print(tmp_A * tmp_B)