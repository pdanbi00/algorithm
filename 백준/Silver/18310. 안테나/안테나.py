# 아이디어 : 집 리스트를 정렬해서 가운데 인덱스에 해당하는 곳에 설치해야 됨.
# 오름차순으로 정렬된 a, b, c, d, e가 있고
# a, b 사이 거리를 x_1, b, c사이 거리를 x_2, c, d 사이 거리를 x_3 등등 이렇게 하고
# a에 설치한 경우는 4x_1 + 3x_2 + 2x_3 + x_4 이런식으로 계산 됨.
# 종이에 적어보면 알게 됨.
N = int(input())
house = list(map(int, input().split()))
house.sort()
print(house[(N-1) // 2])