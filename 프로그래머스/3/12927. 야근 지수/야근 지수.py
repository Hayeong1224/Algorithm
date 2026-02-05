import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    
    for _ in range(n):
        v = heapq.heappop(heap) # 음수 상태
        heapq.heappush(heap, v+1)
        
    return sum(w ** 2 for w in heap)