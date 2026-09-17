from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    time = 0
    cur_weight = 0
    
    while bridge:
        time += 1
        
        # 제일 앞 트럭 빠져나감
        cur_weight -= bridge.popleft()
        
        # 새 트럭 투입
        if waiting:
            if cur_weight + waiting[0] <= weight:
                truck = waiting.popleft()
                bridge.append(truck)
                cur_weight += truck
            else:
                bridge.append(0)
            
    return time