N = int(input())
height = list(map(int, input().split()))
growth = list(map(int, input().split()))

trees = []
for i in range(N):
    trees.append([growth[i], height[i]])
    
trees.sort()

answer = 0
for i in range(N):
    answer += trees[i][0] * i + height[i]

print(answer)