def dfs(i, S, W, broken):
  global result
  if i == N:
    result = max(result, broken)
    return

  # 현재 계란이 꺠졌거나, 나를 제외한 모든 계란이 깨진 경우
  if S[i] <= 0 or broken == N-1:
    dfs(i+1, S, W, broken)
    return
    
  # 현재 계란으로 다른 계란을 칠 수 있는지 확인
  for target in range(N):
    if i != target and S[target] > 0:
      S[target] -= W[i]
      S[i] -= W[target]

      new_broken = 0
      if S[target] <= 0: new_broken += 1
      if S[i] <= 0: new_broken += 1
        
      dfs(i+1, S, W, broken + new_broken)
      
      S[target] += W[i]
      S[i] += W[target]

N = int(input())
S, W = [], []
for i in range(N):
  s, w = map(int, input().split())
  S.append(s)
  W.append(w)

result = 0
dfs(0, S, W, 0)

print(result)