n,m = map(int, input().split())
a, b = [], []
for _ in range(n):
  a.append(list(map(int, input().rstrip())))
for _ in range(n):
  b.append(list(map(int, input().rstrip())))

def flip(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      a[i][j] = 1 - a[i][j]

count = 0
for i in range(n-2):
  for j in range(m-2):
    if a[i][j] != b[i][j]:
      flip(i,j)
      count += 1

match = True
for i in range(n):
  for j in range(m):
      if a[i][j] != b[i][j]:
          match = False
          break

if match:
  print(count)
else:
  print(-1)