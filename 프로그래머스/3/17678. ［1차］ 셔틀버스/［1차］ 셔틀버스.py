from collections import deque

def solution(n, t, m, timetable):
    # 크루들 시간 
    crews = deque(sorted([int(tm[:2]) * 60 + int(tm[3:]) for tm in timetable]))
    
    # 셔틀 버스 시간표
    shuttle_times = [540 + i * t for i in range(n)]
    
    for i, st in enumerate(shuttle_times):
        cnt = 0
        while crews and cnt < m and crews[0] <= st:
            ct = crews.popleft()
            cnt += 1
            
            if i == n - 1 and cnt == m: # 마지막 크루라면 1분 전에 와서 자리 뺏기
                ct -= 1
                return f"{ct // 60:02}:{ct % 60:02}"
            
        if i == n - 1: # 마지막 셔틀이 다 안 찼으면 셔틀 시간에 와도 됨
            return f"{st // 60:02}:{st % 60:02}"