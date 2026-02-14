def solution(strs, t):
    n = len(t)
    dp = [float('inf')] * (n+1) # dp[i]는 t의 i번째 글자까지 만드는데 사용되는 최소 조각의 수
    dp[0] = 0
    
    strs_set = set(strs)
    
    for i in range(1,n+1):
        for j in range(max(0, i-5), i):
            if t[j:i] in strs_set:
                dp[i] = min(dp[i], dp[j] + 1)
                
    return dp[n] if dp[n] != float('inf') else -1