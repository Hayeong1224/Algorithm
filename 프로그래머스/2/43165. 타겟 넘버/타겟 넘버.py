def solution(numbers, target):
    def dfs(i, temp_sum):
        if i == len(numbers):
            return 1 if temp_sum == target else 0
        
        return dfs(i+1, temp_sum + numbers[i]) + dfs(i+1, temp_sum - numbers[i])
    
    return dfs(0,0)