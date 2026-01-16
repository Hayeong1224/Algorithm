n = int(input())

# dp[길이][끝자리] = 끝자리로 끝나는 해당 길의의 계단수 갯수
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
  dp[1][i] = 1

count = 0
for i in range(2, n+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    dp[i][j] %= 1000000000

print(sum(dp[n]) % 1000000000)