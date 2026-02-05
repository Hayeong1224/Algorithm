def solution(s):
    count, deleted = 0, 0
    
    while s != "1":        
        count += 1
        deleted += s.count('0')
        s = str(bin(len(s) - s.count('0')))[2:]
        
    return [count, deleted]