n, w, L = map(int, input().split())
# n : 트럭 수   w : 다리 길이   L : 다리 최대하중
truck = list(map(int, input().split()))
weight = 0 # 현재 다리에 올라와 있는 트럭 무게 합
time = 0
bridge = [0] * w

while True:
    arrive = bridge.pop(0) # 방금 도착한 트럭
    weight -= arrive # 트럭 도착했으니까 현재 다리 무게에서 빼줘야됨

    if truck:
        if weight + truck[0] <= L:
            bridge.append(truck[0])
            weight += truck[0]
            truck.pop(0)
        else:
            bridge.append(0)
    time += 1

    if not bridge:
        break

print(time)