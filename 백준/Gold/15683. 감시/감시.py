import copy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 가능한 방향 조합
modes = [
  [],
  [[0],[1],[2],[3]],
  [[0,2],[1,3]],
  [[0,3],[0,1],[1,2],[2,3]],
  [[0,2,3],[0,1,2],[0,1,3],[1,2,3]],
  [[0,1,2,3]]
]

# cctv 위치
cctvs = []
for i in range(n):
  for j in range(m):
    if 1 <= board[i][j] <= 5:
      cctvs.append((board[i][j], i, j))
      
# 한 방향 직진! 6 만나면 멈춤
def fill(temp_board, x,y,way):    
  while True:
    x += dx[way]
    y += dy[way]
    if not (0<=x<n and 0<=y<m) or temp_board[x][y] == 6:
      break
    if temp_board[x][y] == 0:
      temp_board[x][y] = '#'

ans = float('inf')

def dfs(depth, current_board):
  global ans

  # 모든 cctv 방향 다 결정
  if depth == len(cctvs):
    count = 0
    for row in current_board:
      count += row.count(0)
    ans = min(ans, count)
    return

  # 현재 처리할 cctv 꺼내기
  cctv_num, x, y = cctvs[depth]

  for mode in modes[cctv_num]:
    copy_board = copy.deepcopy(current_board)
    # 해당 모드에 들어있는 모든 방향으로 칠하기
    for way in mode:
      fill(copy_board, x, y, way)
    # 다음 cctv
    dfs(depth+1, copy_board)

dfs(0, board)
print(ans)