def can_fill(r,c,board):
    for i in range(r):
        if board[i][c] != 0:
            return False
    return True

def check(r1, r2, c1, c2, num, board):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if board[r][c] == 0:
                if not can_fill(r,c,board):
                    return False
            elif board[r][c] != num:
                return False
    return True

def solution(board):
    n = len(board)
    blocks_num = 0
    for row in board:
        for val in row:
            if val > blocks_num:
                blocks_num = val
    min_r, max_r = [n] * (blocks_num + 1), [0] * (blocks_num + 1)
    min_c, max_c = [n] * (blocks_num + 1), [0] * (blocks_num + 1)
    existed = [False] * (blocks_num + 1)
    
    for r in range(n):
        for c in range(n):
            num = board[r][c]
            if num != 0:
                existed[num] = True
                min_r[num] = min(min_r[num], r)
                max_r[num] = max(max_r[num], r)
                min_c[num] = min(min_c[num], c)
                max_c[num] = max(max_c[num], c)
    
    cnt = 0
    while True:
        is_changed = False
        for i in range(1, blocks_num + 1):
            if existed[i] and check(min_r[i], max_r[i], min_c[i], max_c[i], i, board):
                for r in range(min_r[i], max_r[i] + 1):
                    for c in range(min_c[i], max_c[i] + 1):
                        if board[r][c] == i:
                            board[r][c] = 0
                
                is_changed = True
                cnt += 1
                existed[i] = False
                break
        
        if not is_changed:
            break
            
    return cnt    