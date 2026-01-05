def solution(n, times):
    start = min(times)
    end = max(times) * n
    answer = 0
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for x in times:
            sum += mid // x
        if sum < n :
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
            
    return answer