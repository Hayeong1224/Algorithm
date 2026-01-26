N = int(input())
student_info = []
like_dict = {}

for _ in range(N**2):
  line = list(map(int, input().split()))
  student_info.append(line[0])
  like_dict[line[0]] = set(line[1:])

board = [[0] * N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for s_id in student_info:
  candidates = []
  for r in range(N):
    for c in range(N):
      if board[r][c] != 0:
        continue

      likes, empties = 0, 0
      for k in range(4):
        nr, nc = r + dx[k], c + dy[k]
        if 0<=nr<N and 0<=nc<N:
          if board[nr][nc] == 0:
            empties += 1
          elif board[nr][nc] in like_dict[s_id]:
            likes += 1
      candidates.append((-likes, -empties, r, c))

  candidates.sort()
  _, _, best_r, best_c = candidates[0]
  board[best_r][best_c] = s_id

ans = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for r in range(N):
  for c in range(N):
    s_id = board[r][c]
    cnt = 0
    for k in range(4):
      nr, nc = r + dx[k], c + dy[k]
      if 0<=nr<N and 0<=nc<N:
        if board[nr][nc] in like_dict[s_id]:
          cnt += 1

    ans += score[cnt]
print(ans)