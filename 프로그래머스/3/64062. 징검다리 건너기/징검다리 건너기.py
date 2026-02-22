def is_enable(stones, k, mid):
    cur_zero = 0
    for s in stones:
        if s < mid:
            cur_zero += 1
            if cur_zero >= k:
                return False
        else:
            cur_zero = 0
    return True

def solution(stones, k):
    left, right = 1, max(stones)
    result = 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_enable(stones, k, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result