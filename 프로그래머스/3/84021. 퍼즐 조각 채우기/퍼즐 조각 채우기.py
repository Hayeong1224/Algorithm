from collections import deque

def extract_shapes(board, target):
    n = len(board)
    shapes = []
    visited = [[False] * n for _ in range(n)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                shape = []
                q = deque([(i,j)])
                visited[i][j] = True
                while q:
                    cx, cy = q.popleft()
                    shape.append((cx,cy))
                    for d in range(4):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            
                # 표준화
                min_x = min(p[0] for p in shape)
                min_y = min(p[1] for p in shape)
                normalized = sorted([(p[0]-min_x, p[1]-min_y) for p in shape])
                shapes.append(normalized)
                
    return shapes

def rotate(shape):
    rotated = [(p[1], -p[0]) for p in shape]
    min_x = min(p[0] for p in rotated)
    min_y = min(p[1] for p in rotated)
    
    return sorted([(p[0]-min_x, p[1]-min_y) for p in rotated])
        
def solution(game_board, table):
    blanks = extract_shapes(game_board, 0)
    puzzles = extract_shapes(table, 1)
    
    ans = 0
    used_puzzles = [False] * len(puzzles)
    
    for blank in blanks:
        found = False
        for i, puzzle in enumerate(puzzles):
            if used_puzzles[i] or len(blank) != len(puzzle):
                continue
            
            #회전
            temp_puzzle = puzzle
            for _ in range(4):
                if blank == temp_puzzle:
                    ans += len(blank)
                    used_puzzles[i] = True
                    found = True
                    break
                temp_puzzle = rotate(temp_puzzle)
            
            if found: break
    
    return ans         