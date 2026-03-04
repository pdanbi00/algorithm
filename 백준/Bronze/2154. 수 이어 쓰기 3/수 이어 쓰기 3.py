N = int(input())
target = str(N)

S = ''.join(str(i) for i in range(1, N+1))
print(S.find(target)+1)