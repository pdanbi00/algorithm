import sys
input = sys.stdin.readline
n = int(input())
people = {}
for i in range(n):
    name, data = input().split()
    if data == "enter":
        people[name] = 1
    elif data == "leave":
        del people[name]
arr = sorted(people.keys(), reverse=True)
for p in arr:
    print(p)