import heapq

def solution(jobs):
    # 작업 번호, 요청 시각, 소요 시간 저장
    # 우선순위: 소요시간 짧음, 요청 시각 빠름, 번호 작음 순
    
    # 1. 요청시각 순으로 정렬
    jobs = sorted((s, l, i) for i, (s, l) in enumerate(jobs))
    
    n = len(jobs)
    
    pq = [] # 대기 중인 작업
    time = 0 # 현재 시간
    idx = 0 # 다음 인덱스
    total = 0 # 반환 시간 총합
    complete = 0 # 완료 작업 수
    
    # 모든 작업 완료할 때까지
    while complete < n:
        # 2. 현재 시각까지 요청된 작업들 우선순위 큐에 넣기
        while idx < n and jobs[idx][0] <= time:
            request, duration, job_id = jobs[idx]
            heapq.heappush(pq, (duration, request, job_id))
            idx += 1
        
        # 3. 대기 중인 작업이 있다면 처리
        if pq:
            duration, request, job_id = heapq.heappop(pq)
            time += duration
            total += (time - request)
            complete += 1
        else: # 4. 대기 중인 작업이 없다면 다음 작업 요청시간으로
            time = jobs[idx][0]
            
    # 5. 평균 반환 시간
    return total // n