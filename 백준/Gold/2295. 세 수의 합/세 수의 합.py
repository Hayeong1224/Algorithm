from itertools import combinations_with_replacement

def solve():
  N = int(input())
  U = [int(input()) for _ in range(N)]
  U.sort(reverse = True)

  # x + y = k - z
  # x + y 조합 만들기
  sums = set()
  for x, y in combinations_with_replacement(U, 2):
    sums.add(x+y)
  
  for k in U:
    for z in U:
      if k - z < 1:
        continue
        
      if (k - z) in sums:
        print(k)
        return

solve()