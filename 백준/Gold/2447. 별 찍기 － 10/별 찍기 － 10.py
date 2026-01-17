def draw_star(n):
  if n == 1:
    return ["*"]

  # n/3 크기의 패턴 구하기
  stars = draw_star(n//3)
  result = []

  # 상단 3 구역
  for s in stars:
    result.append(s*3)
  # 중간 3 구역
  for s in stars:
    result.append(s + ' ' * (n//3) + s)
  # 하단 3 구역
  for s in stars:
    result.append(s*3)

  return result

n = int(input())
print("\n".join(draw_star(n)))