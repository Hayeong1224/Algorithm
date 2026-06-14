def solution(n):
    ln = n * (n+1) // 2
    answer = [[0] * (i+1) for i in range(n)]

    # 아래 - (+1, 0), 오른쪽 - (0, +1), 위 - (-1, -1)
    x, y = 0, 0
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    dir = 0
    for num in range(1, ln + 1):
        answer[x][y] = num
            
        if num == ln: break
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if 0 > nx or nx >= n or 0 > ny or ny >= n or answer[nx][ny] != 0:
            dir = (dir + 1) % 3
            nx = x + dx[dir]
            ny = y + dy[dir] 
                
        x, y = nx, ny
    
    return sum(answer, []) # 이렇게 하면 2차 행렬이 1차로 바뀜