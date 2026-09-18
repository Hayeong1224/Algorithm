def solution(N, number):
    # DP[값]이 아니라 DP[N 사용 개수]
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9): # 최솟값이 8
        # N, NN, NNN, ... 
        dp[i].add(int(str(N)*i))
        
        # j개 사용한 결과 + (i-j)개 사용한 결과
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a // b)
    
        if number in dp[i]:
            return i
    return -1