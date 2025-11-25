def solution(routes): # 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치
    routes.sort(key=lambda x:x[1])
    cameras = 0
    last = -40000
    
    for s, e in routes:
        if last < s or last > e:
            cameras += 1
            last = e
            
    return cameras