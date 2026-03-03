n = int(input())
c, s = 100, 100
for _ in range(n):
  x, y = map(int, input().split())
  if x > y:
    s -= x
  elif x < y:
    c -= y

print(c, s, sep = '\n')