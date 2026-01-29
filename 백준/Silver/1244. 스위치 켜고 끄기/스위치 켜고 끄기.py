N = int(input()) # 스위치 수
switches = list(map(int, input().split()))
M = int(input()) # 학생 수
for _ in range(M):
  g, num = map(int, input().split())
  if g == 1: # 남학생
    for i in range(1,N+1): # 1 2 3 4 5 6 7 8
      if i%num == 0:
        switches[i-1] = 0 if switches[i-1] == 1 else 1

  else: # 여학생
    m, i = num - 1, 1
    switches[m] = 0 if switches[m] == 1 else 1
    while m-i > -1 and m+i < N:
      if switches[m-i] == switches[m+i]:
        switches[m-i] = 0 if switches[m-i] == 1 else 1
        switches[m+i] = switches[m-i]
        i += 1
      else:
        break    
  
for i in range(100):
  if N-1 < i:
    break
  if i > 0 and i%20 == 0:
    print()
  print(switches[i], end=' ')