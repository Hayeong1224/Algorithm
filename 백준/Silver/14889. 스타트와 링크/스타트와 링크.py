from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

members = [i for i in range(n)]
combi = list(combinations(members, n//2))

min_differ = float('inf')

for i in range(len(combi) // 2):
  start = combi[i]
  link = combi[-1 -i] 
  start_s, link_s = 0, 0

  for p1, p2 in combinations(start, 2):
    start_s += s[p1][p2] + s[p2][p1]
  for p1, p2 in combinations(link, 2):
    link_s += s[p1][p2] + s[p2][p1]
    
  min_differ = min(min_differ, abs(start_s - link_s))
  
  if min_differ == 0:
    break
    
print(min_differ)