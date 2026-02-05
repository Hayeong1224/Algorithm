import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for o in operations:
        cmd, num = o.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif len(max_heap) != 0 and cmd == 'D' and num == 1:
            v = heapq.heappop(max_heap)
            min_heap.remove(-v)
        elif len(min_heap) != 0 and cmd == 'D' and num == -1:
            v = heapq.heappop(min_heap)
            max_heap.remove(-v)
            
    if len(min_heap) != 0:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    
    return [0,0]