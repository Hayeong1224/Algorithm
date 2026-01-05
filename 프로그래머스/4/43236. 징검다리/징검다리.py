def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    start = 1
    end = distance
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        current = 0
        
        for rock in rocks:
            if rock - current < mid:
                total += 1
            else:
                current = rock
                
        if total > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
    return answer
        
        