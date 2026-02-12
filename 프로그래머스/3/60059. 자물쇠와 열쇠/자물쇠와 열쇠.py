def rotate(key): # 시계 방향 회전
    return list(map(list,zip(*key[::-1])))

def check(lock):
    n = len(lock) // 3
    for r in range(n, n*2):
        for c in range(n, n*2):
            if lock[r][c] != 1:
                return False
    
    return True

def solution(key, lock):
    n, m = len(lock), len(key)
    
    if key.count(1) < lock.count(0):
        return False
    
    # key가 lock 범위 밖을 자유롭게 다니려면 lock이 커야함! 상하좌우 다 가려면 3배!
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for r in range(n, n*2):
        for c in range(n, n*2):
            new_lock[r][c] = lock[r-n][c-n]
    
    # key 넣어보기
    for r in range(1, n*2):
        for c in range(1, n*2):
            for _ in range(4):
                key = rotate(key)
                for x in range(m):
                    for y in range(m):
                        new_lock[r+x][c+y] += key[x][y]
                        
                if check(new_lock): return True
                
                for x in range(m):
                    for y in range(m):
                        new_lock[r+x][c+y] -= key[x][y]
    
    return False      