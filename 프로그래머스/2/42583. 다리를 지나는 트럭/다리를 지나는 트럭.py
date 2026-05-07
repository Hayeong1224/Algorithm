from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 현재 시간
    q = deque() # 다리 위 트럭 (무게, 나갈 시간)
    nxt = 0 # 다음 트럭
    cur_weights = 0 # 현재 다리 위 트럭 총 무게
    
    while nxt < len(truck_weights) or q:
        answer += 1
        
        # 트럭 나가야 하는지 확인
        if q and q[0][1] == answer:
            w, t = q.popleft()
            cur_weights -= w
            
        # 새로운 트럭: 다리 건너기
        if nxt < len(truck_weights) and cur_weights + truck_weights[nxt] <= weight:
            q.append((truck_weights[nxt], answer + bridge_length))
            cur_weights += truck_weights[nxt]
            nxt += 1
    
    return answer