def drawStar(n):
  if n == 3:
    return ['  *  ', ' * * ', '*****']
  
  stars = drawStar(n//2)
  result = []

  # 위
  for s in stars:
   result.append(' ' * (n//2) + s + ' ' * (n//2))
  # 아래
  for s in stars:
    result.append(s + ' ' + s)

  return result

n = int(input())
print('\n'.join(drawStar(n)))