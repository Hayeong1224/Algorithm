from collections import deque

def solution(n, t, m, timetable):
    shuttle = [(9,0)]
    lh, lm = 9, 0
    for _ in range(n - 1):
        lm += t
        if lm >= 60:
            lh += 1
            lm -= 60
        shuttle.append((lh,lm))
    
    new_t = []
    for t in timetable:
        th, tm = map(int, t.split(':'))
        if th < lh or (th == lh and tm <= lm):
            new_t.append((th,tm))
    new_t.sort(key = lambda x : (x[0], x[1]))
    new_t = deque(new_t)
    
    if not new_t: # 탈 사람 없으면 마지막 셔틀 타기
        ans = f'{lh:02}:{lm:02}'
        return ans
    
    for i in range(len(shuttle)):
        sh, sm = shuttle[i]
        cnt = 0
        while new_t and cnt < m:
            ch, cm = new_t.popleft()
            if sh < ch or (sh == ch and sm < cm): # 크루가 셔틀보다 늦는 경우 제외
                new_t.appendleft((ch,cm))
                break
            cnt += 1
            if i == len(shuttle) - 1 and cnt == m: # 마지막 크루라면 1분 전에 와서 자리 뺏기
                cm -= 1
                if cm < 0:
                    ch -= 1
                    cm += 60
                ans = f'{ch:02}:{cm:02}'
                return ans
            
        if i == len(shuttle) - 1: # 마지막 셔틀이 다 안 찼으면 셔틀 시간에 와도 됨!
            ans = ans = f'{sh:02}:{sm:02}'
            return ans
            
        
        
    
    