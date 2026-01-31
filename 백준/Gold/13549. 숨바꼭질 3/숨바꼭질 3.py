from collections import deque
  
def solve():
  N, K = map(int, input().split())
  dist = [-1] * 100001
  q = deque([N])
  dist[N] = 0

  while q:
    cur = q.popleft()
    if cur == K:
      return dist[K]

    # 순간이동을 걷기보다 먼저 체크 -> 앞에 넣기
    nxt = cur * 2
    if 0<=nxt<=100000 and dist[nxt] == -1:
      dist[nxt] = dist[cur]
      q.appendleft(nxt)

    # 걷기
    for nxt in [cur-1, cur+1]:
      if 0<= nxt <= 100000 and dist[nxt] == -1:
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

print(solve())