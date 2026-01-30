import sys
input = sys.stdin.readline

dp = [1] * 10001 # 1로만 만드는 방법 미리 넣어두기

# 2로 만드는 방법
for i in range(2, 10001):
  dp[i] += dp[i-2]

# 3으로 만드는 방법
for i in range(3, 10001):
  dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
  n = int(input())
  print(dp[n])