N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
distance = []
for i in range(1, N):
    distance.append(sensor[i]-sensor[i-1])
distance.sort()
print(sum(distance[:N-K]))