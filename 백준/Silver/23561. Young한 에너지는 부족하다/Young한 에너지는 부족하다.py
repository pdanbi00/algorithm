N = int(input())
ages = list(map(int, input().split()))
ages.sort()

answer = ages[N+N-1] - ages[N]
print(answer)