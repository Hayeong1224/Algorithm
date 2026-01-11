def solution(arrows):
    move = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    now = (0, 0)
    visited_nodes = {now}
    visited_edges = set()

    count = 0
    
    for arrow in arrows:
        for _ in range(2): # 대각선 교차 예외 문제 해결을 위해 2배로 이동
            next_node = (now[0] + move[arrow][0], now[1]+ move[arrow][1])
            edge = tuple(sorted([now, next_node])) # 경로는 방향이 없으므로 정렬해서 저장
        
            # 처음 가보는 경로인데, 이미 방문한 노드일 때 방 생성
            if next_node in visited_nodes and edge not in visited_edges:
                count += 1
        
            visited_nodes.add(next_node)
            visited_edges.add(edge)
            now = next_node
        
    return count