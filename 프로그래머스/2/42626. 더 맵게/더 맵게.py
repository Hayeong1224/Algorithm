import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2: # 두 개 이상 안 남으면 실패!
            return -1
        
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        new_s = f + s*2
        heapq.heappush(scoville, new_s)
        cnt += 1
    
    return cnt