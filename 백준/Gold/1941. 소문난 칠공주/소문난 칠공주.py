from itertools import combinations
from collections import deque

def is_connected(group):
  q = deque([group[0]])
  visited = {group[0]}
  while q:
    r, c = q.popleft()
    for i in range(4):
      nr, nc = r + dx[i], c + dy[i]
      if (nr,nc) in group and (nr,nc) not in visited:
        visited.add((nr,nc))
        q.append((nr,nc))

  return len(visited) == 7

board = [list(input()) for _ in range(5)]
seats = [(i,j) for i in range(5) for j in range(5)] 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0

for combo in combinations(seats, 7):
  s_count = 0
  for r, c in combo:
    if board[r][c] == 'S':
      s_count += 1

  if s_count >= 4:
    if is_connected(combo):
      cnt += 1

print(cnt)