def check(line):
  used = [False] * N

  for i in range(N-1):
    if line[i] == line[i+1]: # 높이가 같으면 다음 칸으로
      continue

    if abs(line[i] - line[i+1]) > 1:
      return False

    # 내리막
    if line[i] > line[i+1]:
      for j in range(i+1, i+1+L):
        if 0 <= j < N:
          if line[j] != line[i+1] or used[j]: # 연속된 높이가 다르거나 이미 경사로 있으면 x
            return False
          else:
            used[j] = True
        else: # 범위 밖
          return False
          
    # 오르막
    elif line[i] < line[i+1]:
      for j in range(i,i-L,-1):
        if 0 <= j < N:
          if line[j] != line[i] or used[j]:
            return False
          else:
            used[j] = True
        else:
          return False

  return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

count = 0
for r in range(N):
  if check(board[r]):
    count += 1
for c in range(N):
  col = [board[r][c] for r in range(N)]
  if check(col):
    count += 1

print(count)