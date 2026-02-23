def board_sort(board):
  max_len = 0
  new_board = []
  
  for row in board:
    # 0 제외 카운트
    counts = {}
    for num in row:
      if num != 0:
        counts[num] = counts.get(num, 0) + 1

    temp = sorted(counts.items(), key=lambda x : (x[1], x[0]))

    new_row = []
    for n, c in temp:
      new_row.extend([n, c])

    new_row = new_row[:100]
    max_len = max(max_len, len(new_row))
    new_board.append(new_row)

  # 0 채우기
  for row in new_board:
    row.extend([0] * (max_len - len(row)))

  return new_board

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
while cnt <= 100:
  if r-1 < len(board) and c-1 < len(board[0]):
    if board[r-1][c-1] == k:
      print(cnt)
      break

  if cnt == 100:
    print(-1)
    break
  
  if len(board) >= len(board[0]): # R 연산
    board = board_sort(board)

  else: # C 연산: 전치 -> R 연산 -> 전치
    board = list(zip(*board))
    board = board_sort(board)
    board = list(zip(*board))
    
  cnt += 1