N, K = map(int, input().split())
children = list(map(int, input().split()))
diff = []
for i in range(1, N):
    diff.append(children[i] - children[i-1])

diff.sort(reverse=True)

total = sum(diff)
answer = total - sum(diff[:K-1])
print(answer)

'''
9 4
1 2 3 5 7 12 15 16 17
'''