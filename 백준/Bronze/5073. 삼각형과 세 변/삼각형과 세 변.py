while True:
  x, y, z = map(int, input().split())
  if x == y == z == 0:
    break
  m = max(x,y,z)
  if x+y+z - m <= m:
    print("Invalid")
  elif x == y == z:
    print("Equilateral")
  elif (x == y and y != z) or (x == z and x != y) or (y == z and x != z):
    print("Isosceles")
  else:
    print("Scalene")