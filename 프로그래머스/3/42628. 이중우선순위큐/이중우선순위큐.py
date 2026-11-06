import heapq

def solution(operations):
    q = []
    
    for op in operations:
        x, num = op.split()
        num = int(num)
        if x == 'I':
            heapq.heappush(q, num)
    
        elif q:
            if num == 1: # 최댓값 삭제
                q.remove(max(q))
            else: # 최솟값 삭제
                heapq.heappop(q)
    
    return [max(q), heapq.heappop(q)] if q else [0,0]