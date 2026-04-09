def solution(n, times):
    # 모든 사람이 심사 받는데 걸리는 시간의 최솟값
    # (이분 탐색): T라는 시간이 주어졌을 때, 모든 심사관이 최대 몇 명을 심사할 수 있는가?
    answer = 0
    times.sort();
    
    low, high = 0, times[-1] * n
    while low <= high:
        mid = (low + high) // 2
        total = 0
        
        for time in times:
            total += mid // time
            if total >= n: break
            
        if total >= n:
            answer = mid # n명 이상이면 정답 후보
            high = mid - 1
        else:
            low = mid + 1
            
    return answer 