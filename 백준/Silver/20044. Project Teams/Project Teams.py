n = int(input())
student = list(map(int,input().split()))
l = len(student)
student.sort()
# print(student)
teams = [0] * n
cnt = 0
for i in range(l//2):
    # print(student[i], student[l-1])
    teams[cnt%n] += student[i]
    teams[cnt%n] += student[l-1-i]
    cnt += 1
# print(teams)
print(min(teams))