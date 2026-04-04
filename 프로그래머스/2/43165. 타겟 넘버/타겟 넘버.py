def dfs(numbers, target, idx, current_sum):
    if idx == len(numbers):
        return 1 if current_sum == target else 0
    
    total = 0
    total += dfs(numbers, target, idx + 1, current_sum + numbers[idx]) # 덧셈
    total += dfs(numbers, target, idx + 1, current_sum - numbers[idx]) # 뺄셈
    return total

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)