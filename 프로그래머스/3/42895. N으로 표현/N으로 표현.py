def solution(N, number):
    dp = [set() for i in range(9)]
    
    for i in range(1, 9): # N의 개수
        dp[i].add(int(str(N)*  i))
        for j in range(i//2 + 1):
            for op1 in dp[j]: # N을 j번 사용해서 만들 수 있는 숫자들
                for op2 in dp[i-j]: # N을 i - j번 사용해서 만들 수 있는 숫자들
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op2 - op1)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                    if op1 != 0:
                        dp[i].add(op2 // op1)
                        
        if number in dp[i]:
            return i
    
    return -1