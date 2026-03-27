def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for n1 in range(1, n+1):
        for n2 in range(1, n+1):
            if n1 == n2:
                graph[n1][n2] = 0
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for k in range(1, n+1):
        for n1 in range(1, n+1):
            for n2 in range(1, n+1):
                graph[n1][n2] = min(graph[n1][n2], graph[n1][k] + graph[k][n2])

    # 합승 택시 요금 (k가 s인 경우가 따로 따로 가는 경우)
    minfare = INF
    for k in range(1, n+1):
        minfare = min(minfare, graph[s][k] + graph[k][a] + graph[k][b])
        
    return minfare