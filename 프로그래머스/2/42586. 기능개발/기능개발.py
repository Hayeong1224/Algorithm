import math
from collections import deque

def solution(progresses, speeds):
    # 처음 거 기준으로 배포할 때 다음 값들도 배포되는지 확인
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    while progresses:
        job = progresses[0]
        days = math.ceil((100 - job) / speeds[0])

        cnt = 1
        for i in range(1, len(progresses)):
            if progresses[i] + speeds[i] * days >= 100:
                cnt += 1
            else:
                break
        
        answer.append(cnt)

        for i in range(cnt):
            progresses.popleft()
            speeds.popleft()
        
    return answer