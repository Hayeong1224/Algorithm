from itertools import product
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for p in product(arr,repeat=m):
  print(*p)
