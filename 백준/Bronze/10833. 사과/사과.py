N = int(input())
answer = 0
for _ in range(N):
    student, apple = map(int, input().split())
    answer += apple % student

print(answer)