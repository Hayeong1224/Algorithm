from itertools import permutations

def solution(k, dungeons):
    # 최소 필요 피로도, 소모 피로도
    # 최대 던전 수? 다 돌리고 비교하자
    
    # 가능 순서
    order = [i for i in range(len(dungeons))]
    
    max_cnt = 0
    for p in permutations(order, len(dungeons)):
        cnt = 0
        temp_k = k
        
        for i in p:
            if temp_k >= dungeons[i][0]:
                cnt += 1
                temp_k -= dungeons[i][1]
            else:
                break
                
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt