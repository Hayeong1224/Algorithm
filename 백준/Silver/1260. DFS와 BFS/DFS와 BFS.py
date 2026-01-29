from collections import deque

def dfs(start, path, visited):
  for n in nodes[start]:
    if not visited[n]:
      visited[n] = True
      path.append(n)
      dfs(n, path, visited)

  return path

def bfs(start, path):
  visited = [False] * (N+1)
  q = deque([start])
  path.append(start)
  visited[start] = True
  while q:
    v = q.popleft()
    for n in nodes[v]:
      if not visited[n]:
        q.append(n)
        path.append(n)
        visited[n] = True

  return path

N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for i in range(M):
  v1, v2 = map(int, input().split())
  nodes[v1].append(v2)
  nodes[v1].sort()
  nodes[v2].append(v1)
  nodes[v2].sort()

visited = [False] * (N+1)
visited[V] = True
print(*dfs(V, [V], visited))
print(*bfs(V, []))