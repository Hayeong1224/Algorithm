n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0] * 10000
dp[0] = wines[0]

if n > 1:
  dp[1] = wines[0] + wines[1]
  
for i in range(2, n):
  dp[i] = max(dp[i-1],
             dp[i-2] + wines[i],
             dp[i-3] + wines[i-1] + wines[i])

print(dp[n-1])