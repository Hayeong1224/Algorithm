def solution(m, n, puddles):
    d = [[0] * (m+1) for _ in range(n+1)]
    d[1][1] = 1
    
    puddle_set = set((y, x) for x, y in puddles)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i, j) == (1, 1): continue
            if (i, j) in puddle_set:
                d[i][j] = 0
            else:
                d[i][j] = (d[i][j-1] + d[i-1][j]) % 1000000007
    
    return d[n][m]