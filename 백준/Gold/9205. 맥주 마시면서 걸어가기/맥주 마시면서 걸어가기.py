from collections import deque

def bfs():
  n = int(input()) # 맥주 파는 편의점 수
  locations = []
  locations.append(list(map(int, input().split()))) # 출발지
  for _ in range(n):
    locations.append(list(map(int,input().split())))
  locations.append(list(map(int, input().split()))) # 도착지

  visited = [False] * (n+2)

  q = deque([0])
  visited[0] = True

  while q:
    cur = q.popleft()
    cx, cy = locations[cur]

    if cur == n+1: # 페스티벌인지 확인
      print("happy")
      return

    for nxt in range(n+2):
      if not visited[nxt]:
        nxt_x, nxt_y = locations[nxt]
        dist = abs(cx - nxt_x) + abs(cy - nxt_y)

        if dist <= 1000:
          visited[nxt] = True
          q.append(nxt)

  print("sad")  

t = int(input())
for _ in range(t):
  bfs()