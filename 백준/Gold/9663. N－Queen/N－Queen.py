N = int(input())
count = 0

v1 = [False] * N # 열 체크
v2 = [False] * (2*N-1) # 우상향 대각선 체크
v3 = [False] * (2*N-1) # 우하향 대각선 체크

def dfs(r):
  global count
  if r == N:
    count += 1
    return

  for c in range(N):
    # 만약 열, 대각선 중 하나라도 퀸이 있다면 건너뛰기
    if not v1[c] and not v2[r+c] and not v3[r-c+(N-1)]:
      v1[c] = v2[r+c] = v3[r-c+(N-1)] = True
      
      dfs(r+1)
      
      v1[c] = v2[r+c] = v3[r-c+(N-1)] = False

dfs(0)
print(count)