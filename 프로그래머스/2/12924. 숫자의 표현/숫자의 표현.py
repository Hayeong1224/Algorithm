def solution(n):
    answer = 1 # 자기 자신
    for i in range(1, n//2 + 1):
        temp_sum, temp_i = i, i
        while temp_sum < n:
            temp_i += 1
            temp_sum += temp_i
        
        if temp_sum == n:
            answer += 1
    
    return answer