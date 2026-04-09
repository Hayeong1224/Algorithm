import heapq
def solution(operations):
    answer = []
    
    minq = []
    maxq = []
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
        elif minq and maxq:
            if num == -1:
                heapq.heappop(minq)
                del maxq[-1]
            else:
                heapq.heappop(maxq)
                del minq[-1]
    
    return [-maxq[0], minq[0]] if minq and maxq else [0,0]