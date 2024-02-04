N = int(input())
people = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append([i, age, name])
people.sort(key=lambda x: (x[1], x[0]))
for person in people:
    print(person[1], person[2])