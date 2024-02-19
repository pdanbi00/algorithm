# 달팽이는 낮에 나무 막대에 다 올라갈거임
# k일에 도달한다고 하면 올라가는 횟수는 k번, 내려오는 횟수는 k-1번
# 총 올라간거는 V = Ak - B(k-1)
# k = (V-B) / (A-B)
# 이 값이 정수라면 k일에 다 올라간거임.
# 이 값이 정수가 아니면 하루 더 지나서 올라갈거임
A, B, V = map(int, input().split())
x = (V-B) / (A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)