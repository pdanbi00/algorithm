from itertools import combinations

def solution(line):
  points = []
  # 1. 모든 직선의 조합을 확인하여 교점 구하기
  for line1, line2 in combinations(line, 2):
    A, B, C = line1
    D, E, F = line2

    divider = A * E - B * D
    # 평행하거나 일치하는 경우 제외
    if divider == 0:
      continue

    x = (B * F - E * C) / divider
    y = (C * D - A * F) / divider

    if x.is_integer() and y.is_integer():
      points.append((int(x), int(y)))

  min_x = min(p[0] for p in points)
  max_x = max(p[0] for p in points)
  min_y = min(p[1] for p in points)
  max_y = max(p[1] for p in points)

  width = max_x - min_x + 1
  height = max_y - min_y + 1
  grid = [['.' ] * width for _ in range(height)]

  for x, y in points:
    grid[max_y - y][x - min_x] = '*'

  return [''.join(row) for row in grid]