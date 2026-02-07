import heapq
def solution(jobs):
    ans, now, i = 0, 0, 0
    start = -1
    waiting = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(waiting, [j[1], j[0]])
        
        if waiting:
            cur = heapq.heappop(waiting)
            start = now
            now += cur[0]
            ans += now - cur[1]
            i += 1
        else:
            now += 1
            
    return ans // len(jobs)
            
                
                
        