import math

t = int(input())
for _ in range(t):
  x, y = map(int, input().split())
  dist = y - x

  n = int(math.sqrt(dist)) #n은 최대 속도

  if n ** 2 == dist: #제곱수일 때
    print(2*n - 1)
  elif dist <= n**2 + n:
    print(2*n)
  else:
    print(2*n + 1)