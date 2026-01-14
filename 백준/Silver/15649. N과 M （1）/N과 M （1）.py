from itertools import permutations
N, M = map(int, input().split())
array = [i for i in range(1, N+1)]

p = permutations(array, M)
for t in p:
  print(*t)