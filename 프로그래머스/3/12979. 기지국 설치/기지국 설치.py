import math
def solution(n, stations, w):
    # 기지국들을 기준으로 나누고 나눈 거마다 길이를 재서 필요한 기지국 수 구하기!
    cnt = 0
    prev = 1
    range_w = 2 * w + 1
    
    for s in stations:
        length = (s - w) - prev
        
        if length > 0:
            cnt += math.ceil(length / range_w)
        
        prev = s + w + 1
    
    if prev <= n:
        length = n - prev + 1
        cnt += math.ceil(length / range_w)
    
    return cnt