n, m = map(int, input().split())
path = []

def dfs(start):
  if len(path) == m:
    print(*path)
    return

  for i in range(start, n+1):
    path.append(i)
    dfs(i)
    path.pop()

dfs(1)