from collections import deque

def bfs(start):
  dist = [-1] * (F+1)

  q = deque([start])
  dist[start] = 0

  while q:
    cur = q.popleft()

    if cur == G:
      return dist[cur]
    
    for d in [U, -D]:
      if 0<cur+d<=F and dist[cur+d] == -1:
        dist[cur+d] = dist[cur] + 1
        q.append(cur+d)

  return "use the stairs"
  

F, S, G, U, D = map(int, input().split())
print(bfs(S))