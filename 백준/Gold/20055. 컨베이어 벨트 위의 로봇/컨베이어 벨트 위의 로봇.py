from collections import deque

N, K = map(int, input().split())
conveyor = deque(map(int, input().split())) #2N개
robots = deque([False] * N)

ans = 0

while True:
  ans += 1

  # 벨트와 로봇 이동
  conveyor.rotate(1)
  robots.rotate(1)
  robots[N-1] = False # 내리기

  # 로봇 한 칸 이동
  for i in range(N-2, -1, -1):
    if robots[i] and not robots[i+1] and conveyor[i+1] > 0:
      robots[i] = False
      robots[i+1] = True
      conveyor[i+1] -= 1
  robots[N-1] = False

  # 로봇 올리기
  if conveyor[0] > 0:
    robots[0] = True
    conveyor[0] -= 1

  # 내구도 검사
  if conveyor.count(0) >= K:
    break
  
print(ans)