from collections import deque

N = int(input())
K = int(input())
visited = [False] * N
computers = [[] for _ in range(N)]
for _ in range(K):
  a, b = map(int, input().split())
  computers[a-1].append(b-1)
  computers[b-1].append(a-1)

q = deque([0])
visited[0] = True
while q:
  c = q.popleft()
  for nc in computers[c]:
    if not visited[nc]:
      visited[nc] = True
      q.append(nc)

print(visited.count(True) - 1) # 1번 컴퓨터 제외