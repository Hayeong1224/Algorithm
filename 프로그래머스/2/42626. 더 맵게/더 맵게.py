import heapq

def solution(scoville, K):
    answer = 0
    
    # 정렬하고 다시 만들고 정렬하고 반복 -> 오래 걸림 
    # heap에 넣기~~
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1

    return answer