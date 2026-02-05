A, B = input().split()

big_A = ''
small_A = ''

big_B = ''
small_B = ''

for i in range(len(A)):
    if A[i] == '5':
        big_A += '6'
        small_A += '5'
    elif A[i] == '6':
        big_A += '6'
        small_A += '5'
    else:
        big_A += A[i]
        small_A += A[i]


for i in range(len(B)):
    if B[i] == '5':
        big_B += '6'
        small_B += '5'
    elif B[i] == '6':
        big_B += '6'
        small_B += '5'
    else:
        big_B += B[i]
        small_B += B[i]


print(int(small_A) + int(small_B), int(big_A) + int(big_B))