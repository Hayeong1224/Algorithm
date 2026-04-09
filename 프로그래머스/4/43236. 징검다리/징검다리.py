def solution(distance, rocks, n):
    answer = 0
    
    # 거리 최솟값(기준)의 최댓값 -> 일단 제거할 바위 n 개 골라야 함.
    # 거리가 도저히 그냥 탐색할 순 없이 길다 -> parametric search
    # 바위 거리 사이가 최소(mid) 이상이려면, 바위를 몇 개 빼야 하는 가? -> n보다 작거나 같다면 가능
    rocks.sort()
    rocks.append(distance)
    
    low = 1
    high = distance
    
    while low <= high:
        mid = (low + high) // 2
        prev = 0    # 이전 바위 위치
        removed = 0 # 제거한 바위 개수
        
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed += 1
            else:
                prev = rocks[i]
                
        if removed <= n:    # n개 이하로 제거해서 mid를 유지할 수 있다면, 더 큰 mid도 시도
            answer = mid
            low = mid + 1
        else:   # 제거한 바위가 n개보다 많으면, mid가 너무 큰 것이므로 줄이기
            high = mid - 1
    
    return answer