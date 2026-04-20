from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    answer = [0] * len(priorities)
    
    t = 1
    while q:
        mq = max(q, key = lambda x : x[1])
        mp = mq[1]
        i, p = q.popleft()

        if p == mp: # 실행
            answer[i] = t
            t += 1
        else:
            q.append((i,p))
            
    return answer[location]