def solution(n):
    dp = [1,1,2,5] + [0] * (n - 3)
    for i in range(4, n+1):
        v = 0
        for j in range(0, i+1):
            v += dp[j] * dp[i-j-1]
        dp[i] = v
        
    return dp[n]