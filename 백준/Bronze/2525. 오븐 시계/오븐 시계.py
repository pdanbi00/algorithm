A, B = map(int, input().split())
C = int(input())
time = A * 60 + B
time += C
time %= (24 * 60)
hour = time // 60
time -= hour * 60
print(hour, time)