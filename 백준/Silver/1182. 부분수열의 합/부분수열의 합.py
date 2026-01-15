from itertools import combinations

N, S = map(int, input().split())
seq = list(map(int, input().split()))

count = 0
for i in range(1,N+1):
  for p in combinations(seq, i):
    sum = 0
    for j in p:
      sum += j
    if sum == S:
      count += 1

print(count)