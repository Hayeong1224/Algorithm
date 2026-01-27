import sys
input = sys.stdin.readline

# 모든 선이 제자리로 오는지
def check():
  for start in range(1,N+1):
    current_pos = start
    for h in range(1, H+1):
      if board[h][current_pos]:
        current_pos += 1
      elif board[h][current_pos-1]:
        current_pos -= 1
    if current_pos != start:
      return False
  return True

# 가로선 놓기
def dfs(cnt, r, c):
  global ans
  if check():
    ans = min(ans, cnt)
    return

  # 이미 3개 놓았거나, 현재 찾은 최솟값보다 많이 놓아야 하면 종료
  if cnt == 3 or cnt >= ans:
    return

  for i in range(r, H+1):
    # 같은 행에서 다음 열부터 탐색
    start_c = c if i == r else 1
    for j in range(start_c, N):
      if not board[i][j] and not board[i][j-1] and not board[i][j+1]:
        board[i][j] = 1
        dfs(cnt + 1, i, j + 2)
        board[i][j] = 0



N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
  
for _ in range(M):
  a, b = map(int,input().split()) # b와 b+1 세로선을 a번 점선에서 연결
  board[a][b] = 1

ans = 4
dfs(0, 1, 1)
print(ans if ans < 4 else -1)