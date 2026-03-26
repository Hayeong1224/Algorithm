def move(fireballs):
  new_grid = {} # (r,c)는 키, 파이어볼 리스트를 값으로
  for r, c, m, s, d in fireballs:
    nr = (r + dr[d] * s) % N
    nc = (c + dc[d] * s) % N
    if (nr, nc) not in new_grid:
      new_grid[(nr,nc)] = []
    new_grid[(nr,nc)].append((m, s, d))
  return new_grid

def checkBalls(grid):
  global fireballs
  new_fireballs = []
  
  for (r,c), balls in grid.items():
    if len(balls) == 1:
      m, s, d = balls[0]
      new_fireballs.append([r,c,m,s,d])
    else:
      sm, ss, cnt = 0, 0, len(balls)
      odds, evens = 0, 0
      for m, s, d in balls:
        sm += m
        ss += s
        if d % 2 == 0: evens += 1
        else: odds += 1
      nm = sm // 5
      if nm == 0: continue
      ns = ss // cnt

      dirs = [0,2,4,6] if evens == cnt or odds == cnt else [1,3,5,7]
      for nd in dirs:
        new_fireballs.append([r,c,nm,ns,nd])
  fireballs = new_fireballs

N, M, K = map(int, input().split())
fireballs = [] 
for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  fireballs.append([r-1, c-1, m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
  grid = move(fireballs)
  checkBalls(grid)

print(sum(f[2] for f in fireballs))