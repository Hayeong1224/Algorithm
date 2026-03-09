def solution(board, skill):
    n = len(board)
    m = len(board[0])
    temp = [[0] * (m+1) for _ in range(n+1)]
     
    for type, r1, c1, r2, c2, degree in skill:
        val = ((-1) ** type) * degree
        temp[r1][c1] += val
        temp[r1][c2 + 1] -= val
        temp[r2 + 1][c1] -= val
        temp[r2 + 1][c2 + 1] += val
        
    for r in range(n + 1):
        for c in range(1, m + 1):
            temp[r][c] += temp[r][c-1]
            
    for c in range(m + 1):
        for r in range(1, n + 1):
            temp[r][c] += temp[r-1][c]
    
    ans = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + temp[r][c] > 0:
                ans += 1
                
    return ans