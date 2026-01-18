from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]

def bfs(k,start):
  q = deque([start])
  visited = [False] * (N+1)
  visited[start] = True
  count = 0
  
  while q:
    cur = q.popleft()
    
    for n, usado in adj[cur]:
      if not visited[n] and usado >= k:
        q.append(n)
        visited[n] = True
        count += 1

  print(count)   

for _ in range(N-1):
  p, q, r = map(int, input().split()) # p와 q가 유사도 r로 서로 연결되어 있음
  adj[p].append([q,r])
  adj[q].append([p,r])

for _ in range(Q):
  k, v = map(int, input().split())
  bfs(k,v)