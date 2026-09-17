def solution(numbers, target):
    
    def dfs(idx, cur):
        # 종료 조건
        if idx == len(numbers):
            if target == cur:
                return 1
            else:
                return 0
        
        cnt = 0
        nxt = numbers[idx]
        
        # +
        cnt += dfs(idx+1, cur + nxt)
        
        # -
        cnt += dfs(idx+1, cur - nxt)
        return cnt
    
    return dfs(0, 0)