import heapq

def solution(board):
    n = len(board)
    dist = [[[float('inf')] * n for _ in range(n)] for _ in range(4)]
    pq = [] # 우선순위 큐(cost, x, y, dir)
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    if board[0][1] == 0:
        heapq.heappush(pq, (100,0,1,0))
        dist[0][0][1] = 100
    if board[1][0] == 0:
        heapq.heappush(pq, (100,1,0,1))
        dist[1][1][0] = 100
    
    while pq:
        cost, cx, cy, d = heapq.heappop(pq)
        
        if dist[d][cx][cy] < cost:
            continue
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                new_cost = cost + (100 if i == d else 600)
                
                if new_cost < dist[i][nx][ny]:
                    dist[i][nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, i))
                
    return min(dist[i][n-1][n-1] for i in range(4))