from collections import deque

# 한 칸 움직임
def move(direction):
  # 0번째는 꼬리 -> append() - 헤드, popleft() - 꼬리
  headx, heady = snake[-1]
  nheadx, nheady = headx + dx[direction], heady + dy[direction]
  # 벽이라면?
  if nheadx<0 or N<=nheadx or nheady<0 or N<=nheady:
    return False

  else:
    # 몸이라면?
    if (nheadx, nheady) in snake:
      return False
      
    # 몸통 늘려서 다음 칸에 위치
    snake.append((nheadx,nheady))
    
    # 사과라면?
    if (nheadx, nheady) in apples:
      apples.pop((nheadx, nheady))
    else:
      snake.popleft()

  return True


#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
K = int(input())
apples = {}
for _ in range(K):
  r,c = map(int, input().split())
  apples[(r-1,c-1)] = True
L = int(input()) # 방향 변환 횟수
dir_change = {} # 딕셔너리 
for _ in range(L):
  x, c = list(input().split())
  dir_change[int(x)] = c

snake = deque([(0,0)])

count = 0
dir = 0 # 처음은 오른쪽
while True:
  count += 1
  
  if not move(dir):
    print(count)
    break

  if count in dir_change:
    if dir_change[count] == 'D':
      dir = (dir+1) % 4
    else:
      dir = (dir+3) % 4