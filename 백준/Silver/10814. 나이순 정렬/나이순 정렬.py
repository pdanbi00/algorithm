N = int(input())
people = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append([age, name])
# 파이썬은 기본적으로 stable 정렬을 함.
# 그래서 기준을 주는대로 정렬하되 처음 들어온 순서를 유지하면서 함.
# 예를 들어, [1, 2, 3(X), 4, 5, 3(Y)] 을 오름차순 정렬한다면,
# [1, 2, 3(X), 3(Y), 4, 5]순으로 세 번째 위치한 3의 위치와 여섯 번째 위치한 3의 위치가 바뀌지 않는다.
people.sort(key=lambda x: x[0])
for person in people:
    print(person[0], person[1])