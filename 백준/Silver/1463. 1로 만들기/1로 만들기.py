def solve():
  n = int(input())
  dp = [0] * (n + 1)

  if n == 1:
    print(0)
    return 

  for i in range(2, n+1):
    x = dp[i//3] if i % 3 == 0 else 10 ** 6
    y = dp[i//2] if i % 2 == 0 else 10 ** 6 
    z = dp[i-1]
      
    dp[i] = min(x,y,z) + 1

  print(dp[n])
    
solve()