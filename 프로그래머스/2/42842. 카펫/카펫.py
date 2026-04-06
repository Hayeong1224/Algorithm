def solution(brown, yellow):
    rc = brown + yellow
    
    # r이 c보다 작을 수 밖에 없음!
    for r in range(3, int(rc**0.5) + 1):
        if rc % r == 0:
            c = rc // r
            
            if (r-2) * (c-2) == yellow:
                return [c, r]