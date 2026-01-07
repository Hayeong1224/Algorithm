def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)
    
    max_d = [[-float('inf')] * n for _ in range(n)]
    min_d = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        max_d[i][i] = min_d[i][i] = nums[i]
    
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            for k in range(i,j):
                if ops[k] == '+':
                    max_d[i][j] = max(max_d[i][j], max_d[i][k] + max_d[k+1][j])
                    min_d[i][j] = min(min_d[i][j], min_d[i][k] + min_d[k+1][j])
                else:
                    max_d[i][j] = max(max_d[i][j], max_d[i][k] - min_d[k+1][j])
                    min_d[i][j] = min(min_d[i][j], min_d[i][k] - max_d[k+1][j])
    
    return max_d[0][n-1]