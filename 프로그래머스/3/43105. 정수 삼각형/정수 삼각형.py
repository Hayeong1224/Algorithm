def solution(triangle):
    # 아래에서 위로
    n = len(triangle) - 1
    
    for i in range(n, 0, -1): # n, n-1, n-2, ... , 1
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
            
    return triangle[0][0]