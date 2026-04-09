import heapq

def solution(jobs):
    pq = []
    now, n = 0, len(jobs)
    i = 0 # 처리한 job의 수
    start = -1
    total_return_time = 0 # 반환 시간
    
    indexed_jobs = []
    for idx, job in enumerate(jobs):
        indexed_jobs.append([job[0], job[1], idx])
    indexed_jobs.sort()
    
    
    while i < n:        
        # 소요시간이 짧은 것, 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위 높음
        for j_ask_time, j_term_time, j_idx in indexed_jobs:
            if start < j_ask_time <= now:
                heapq.heappush(pq, (j_term_time, j_ask_time, j_idx))
            elif j_ask_time > now: break
        
        if len(pq) > 0: # 작업 시작
            term_time, ask_time, _ = heapq.heappop(pq)
            start = now
            now += term_time
            total_return_time += (now - ask_time)
            i += 1
        else: # 다음 작업 시간으로 점프
            now = indexed_jobs[i][0]
        
    return total_return_time // n