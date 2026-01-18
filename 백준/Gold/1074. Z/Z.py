n, r, c = map(int, input().split())
count = 0

def dfs(n,x,y):
  global count
  if n == 0:
    return

  half = 2**(n-1)
  size = half * half

  # 1, 2, 3, 4사분면
  if r < x+half and c < y+half:
    dfs(n-1, x, y)

  elif r < x+half and c >= y+half:
    count += size
    dfs(n-1,x,y+half)

  elif r >= x+half and c < y+half:
    count += size*2
    dfs(n-1, x+half, y)

  else:
    count += size*3
    dfs(n-1,x+half,y+half)

dfs(n,0,0)
print(count)