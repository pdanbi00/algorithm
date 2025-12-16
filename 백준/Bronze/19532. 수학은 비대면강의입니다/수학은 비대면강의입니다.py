a, b, c, d, e, f = map(int, input().split())

y = (c * d - f * a) / (b * d - e * a)
x = (c * e - b * f) / (a * e - b * d)

print(int(x), int(y))