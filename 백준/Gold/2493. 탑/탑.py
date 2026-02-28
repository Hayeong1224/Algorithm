from collections import deque

n = int(input())
tops = list(map(int, input().split()))

q = deque()
result = []
for i, top in enumerate(tops):
  exist = False
  while q:
    prev_top, prev_num = q.popleft()
    
    if prev_top >= top:
      result.append(prev_num)
      q.appendleft((prev_top, prev_num))
      exist = True
      break
      
  if not exist: result.append(0)
  q.appendleft((top, i+1))

print(*result)