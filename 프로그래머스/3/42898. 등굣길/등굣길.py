def solution(m, n, puddles):
    # (1,1) -> (m,n)
    # 오, 아
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for y, x in puddles:
        dp[x][y] = -1
    
    # 집에서 학교까지 갈 수 있는 최단경로의 개수
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            
            up = dp[i-1][j]
            left = dp[i][j-1]
            dp[i][j] = (up + left) % 1000000007
    
    return dp[n][m]