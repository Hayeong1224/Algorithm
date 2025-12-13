def solution(brown, yellow):
    answer = list()
    rc = brown+yellow
    for r in range(3,brown//2):
        c = rc // r
        if (r-2) * (c-2) == yellow:
            return [c,r]