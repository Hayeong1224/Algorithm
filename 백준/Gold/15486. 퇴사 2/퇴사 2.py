N = int(input())
T, P = [], []
for i in range(N):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

dp = [0] * N
for i in range(N-1, -1, -1):
  a, b, c = 0, 0, 0
  if i != N-1:
    a = dp[i+1]
  
  if i + T[i] == N:
    b = P[i]

  if i + T[i] < N:
    c = P[i] + dp[i + T[i]]
  
  dp[i] = max(a,b,c)

print(max(dp))