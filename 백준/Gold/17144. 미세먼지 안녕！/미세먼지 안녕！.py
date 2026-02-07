def spread():
  new_A = [[0] * C for _ in range(R)]
  for r in m_pos:
    new_A[r][0] = -1

  for r in range(R):
    for c in range(C):
      if A[r][c] not in [-1, 0]:
        cnt = 0
        for i in range(4):
          nr, nc = r + dr[i], c + dc[i]
          if 0<=nr<R and 0<=nc<C and A[nr][nc] != -1:
            new_A[nr][nc] += A[r][c] // 5
            cnt += 1

        new_A[r][c] += A[r][c] - (A[r][c]//5) * cnt

  return new_A

def operate():
  global A
  # 1. 위 - 반시계방향 청정 (반대로 훑기 - 상 -> 우 -> 하 -> 좌)
  x = m_pos[0]
  
  for i in range(x-1,0,-1): # 상
    A[i][0] = A[i-1][0]
  
  for i in range(0,C-1): # 우
    A[0][i] = A[0][i+1]
  
  for i in range(0,x): # 하
    A[i][C-1] = A[i+1][C-1]
  
  for i in range(C-1,1,-1): # 좌
    A[x][i] = A[x][i-1]
    
  A[x][1] = 0 # 한 칸 밀기

  # 2. 아래 - 시계방향 청정 (반대로 훑기 - 하 -> 우 -> 상 -> 좌)
  x = m_pos[1]
  
  for i in range(x+1,R-1): # 하
    A[i][0] = A[i+1][0]
  
  for i in range(0,C-1): # 우
    A[R-1][i] = A[R-1][i+1]
  
  for i in range(R-1,x,-1): # 상
    A[i][C-1] = A[i-1][C-1]
  
  for i in range(C-1,1,-1): # 좌
    A[x][i] = A[x][i-1]
  
  A[x][1] = 0 

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

# 청정기 위치 찾기
m_pos = []
for r in range(R):
  if A[r][0] == -1:
      m_pos.append(r)
      m_pos.append(r+1)
      break

dr = [0,1,0,-1] #우, 하, 좌, 상
dc = [1,0,-1,0]

for _ in range(T):
  # 먼지 확산
  A = spread()
  # 공기청정기 작동
  operate()

ans = 0
for r in range(R):
  ans += sum(A[r])
print(ans+2) # 공기청정기 제외