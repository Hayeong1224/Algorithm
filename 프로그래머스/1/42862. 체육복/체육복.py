def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # 자기자신 제외
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
     
    # 앞뒤에서 빌리는 거 제외
    for x in _reserve:
        f = x - 1
        b = x + 1
        
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    
    return n - len(_lost)