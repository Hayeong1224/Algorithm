def solution(nums):
    types = {}
    for n in nums:
        types[n] = types.get(n, 0) + 1
        
    n = len(nums) // 2
    
    if len(types) >= n:
        return n
    
    else:
        return len(types)