def solution(n, money):
    dp = [0] * (n + 1)
    
    dp[0] = 1 # 아무것도 선택하지 않음
    
    for coin in money:
        # i원을 만드는 법 = (기존 방법) + (i - coin원을 만드는 방법)
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin] 
            
    return dp[n]