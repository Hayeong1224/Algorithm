N, K = map(int, input().split())
items = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

#dp[물건번호][무게]
dp = [[0] * (K+1) for _ in range(N+1 )]

for i in range(1, N+1):
  w, v = items[i]
  for j in range(1, K+1):
    if j < w:
      # 현재 배낭 용량이 물건 무게보다 작으면 못 넣음 -> 유지
      dp[i][j] = dp[i-1][j]
    else:
      # 안 넣음 vs 현재 물건 가치 + 남은 무게에 대한 이전 최적값 
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])