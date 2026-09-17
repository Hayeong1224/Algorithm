from collections import deque

def solution(n, computers):
    answer = 0
    in_net = set()
    
    for i in range(len(computers)):
        if i not in in_net: # 그룹 찾아가자~~
            answer += 1
            
            q = deque([i])
            
            while q:
                cur = q.popleft()
                in_net.add(cur)
                
                for idx, check in enumerate(computers[cur]):
                    if check and idx not in in_net:
                        q.append(idx)
    
    return answer