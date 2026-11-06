def solution(N, number):
    dp = [set() for _ in range(9)]
    # dp[i]의 i가 답이 될 수 있게 구성 - 사용 횟수
    
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
        # j개 사용한 결과 + i-j개 사용한 결과
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        
        if number in dp[i]:
            return i
        
    return -1