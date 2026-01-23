from collections import deque
board = [list(input()) for _ in range(12)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 터뜨리기
def play():
  global board
  visited = [[False] * 6 for _ in range(len(board))]
  is_popped = False # 이번 턴에 터진게 있는지 확인
  
  for i in range(12):
    for j in range(6):
      if board[i][j] != '.' and not visited[i][j]:
        color = board[i][j]
        q = deque([(i,j)])
        visited[i][j] = True
        temp_list = [(i,j)]
        
        while q:
          x, y = q.popleft()
          for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and color == board[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                temp_list.append((nx,ny))
              
        if len(temp_list) >= 4: # 터뜨려야지
          is_popped = True 
          for tx, ty in temp_list:
            board[tx][ty] = '.'
          
  return is_popped

# 떨어지기
def drop():
  global board
  for c in range(6):
    new_col = [] # 밑에서부터 뿌요만 모으기
    for r in range(11, -1, -1):
      if board[r][c] != '.':
        new_col.append(board[r][c])

    # 보드를 밑에서부터 뿌요로 채우고 위에는 . 채우기
    for r in range(11, -1, -1):
      if len(new_col) > 0:
        board[r][c] = new_col.pop(0)
      else:
        board[r][c] = '.'

ans = 0
while True:
  if play():
    ans += 1
    drop()
  else:
    break
    
print(ans)