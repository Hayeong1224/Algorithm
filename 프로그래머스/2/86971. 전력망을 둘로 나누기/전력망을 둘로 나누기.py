from collections import deque

def solution(n, wires):
    min_diff = len(wires)
    
    for [w1, w2] in wires: # 하나씩 끊어보자
        print(f"{w1, w2} 끊음")
        new_wires = [w for w in wires if w != [w1, w2]]
        visited = [False] * (n+1)
        
        q = deque([new_wires[0][0]])
        visited[new_wires[0][0]] = True
        cnt = 1
        
        while q:
            cur = q.popleft()
            print(f"{cur} 방문")
            for nw1, nw2 in new_wires: # 단방향이니까 양방향 확인
                if cur == nw1 and not visited[nw2]:
                    visited[nw2] = True
                    print(nw1, nw2)
                    q.append(nw2)
                    cnt += 1
                elif cur == nw2 and not visited[nw1]:
                    visited[nw1] = True
                    print(nw2, nw1)
                    q.append(nw1)
                    cnt += 1
        
        min_diff = min(min_diff, abs(cnt - (n - cnt)))
        
        print(f"차이: {abs(cnt - (n - cnt))}, 현재 min: {min_diff}")
        
    return min_diff
                