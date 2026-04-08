def solution(arrows):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    
    # 방 생성 기준? 선으로 둘러 싸임 - 다른 방향을 또 들어오면 방 하나?
    now = (0,0)
    visited_nodes = {now}
    visited_edges = set()
    
    ans = 0
    for i in arrows:
        # 두 칸 이동
        for _ in range(2):
            nxt_node = (now[0] + dx[i], now[1] + dy[i])
            
            # 방이 생성되는 조건 확인
            if nxt_node in visited_nodes:
                # 이미 방문한 노드인데, 처음 가는 경로면 방 + 1
                if (now, nxt_node) not in visited_edges:
                    ans += 1
                    
            visited_nodes.add(nxt_node)
            # 간선 양방향 저장
            visited_edges.add((now, nxt_node))
            visited_edges.add((nxt_node, now))
            
            now = nxt_node
        
    return ans