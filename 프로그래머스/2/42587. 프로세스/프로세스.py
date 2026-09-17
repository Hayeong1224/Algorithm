from collections import deque

def solution(priorities, location):
    q = deque([(p,i) for i, p in enumerate(priorities)])
    cnt = 0
    
    while priorities:
        # max값을 찾기
        max_p = max(q, key = lambda x : x[0])
        idx = q.index(max_p)
        
        # max값이 제일 앞에 올 때까지 왼쪽으로 보냄
        q.rotate(-idx)
    
        # max 실행
        p, i = q.popleft()
        cnt += 1
        
        if i == location: 
            return cnt