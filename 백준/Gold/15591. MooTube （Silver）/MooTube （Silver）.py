from collections import deque

N, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]

def bfs(k,v):
  
  q = deque([(v,0)])
  visited[v] = True
  while q:
    cur, u = q.popleft()
    
    for n, usado in adj[cur]:
      if not visited[n] and usado >= k:
        q.append((n, usado))
        visited[n] = True

  print(visited.count(True) - 1)   

for _ in range(N-1):
  p, q, r = map(int, input().split()) # p와 q가 유사도 r로 서로 연결되어 있음
  adj[p].append([q,r])
  adj[q].append([p,r])

for _ in range(Q):
  k, v = map(int, input().split())
  visited = [False] * (N+1)
  # 답 계산
  bfs(k,v)