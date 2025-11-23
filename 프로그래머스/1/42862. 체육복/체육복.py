def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    new = []
    # 자기자신 제외 (lost에서 삭제하면 한 칸씩 앞으로 와서 삭제가 제대로 안 됨 -> 중복이 아니면 new에 넣기)
    for x in lost:
        if x in reserve:
            reserve.remove(x)
        else:
            new.append(x)
    
    answer = n - len(new)
            
    # 앞뒤에서 빌리는 거 제외
    for x in new:
        if reserve.count(x-1) > 0:
            reserve.remove(x-1)
            answer += 1
        elif reserve.count(x+1) > 0:
            reserve.remove(x+1)
            answer += 1    
    
    return answer