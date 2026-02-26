from collections import deque

n, m = map(int, input().split())
move = {}
for _ in range(n + m):
  x, y = map(int, input().split())
  move[x] = y

visited = [-1] * 101
q = deque([1])
visited[1] = 0

while q:
  cur = q.popleft()

  if cur == 100:
    print(visited[100])
    break

  for dice in range(1,7):
    nxt = cur + dice

    if nxt <= 100:
      if nxt in move:
        nxt = move[nxt]

      if visited[nxt] == -1:
        visited[nxt] = visited[cur] + 1
        q.append(nxt)