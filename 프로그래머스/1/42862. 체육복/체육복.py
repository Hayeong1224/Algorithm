def solution(n, lost, reserve):
    overlap = set(lost) & set(reserve) # 겹치는 학생
    
    lost = sorted(set(lost) - overlap)
    reserve = set(reserve) - overlap
    
    ans = n - len(lost)
    
    for l in lost:
        if l-1 in reserve:
            ans += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            ans += 1
            reserve.remove(l+1)

    return ans