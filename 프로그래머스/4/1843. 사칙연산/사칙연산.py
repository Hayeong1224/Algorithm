INF = 1e9
def solution(arr):
    # 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 함 -> 최대값과 최솟값 계산
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    N = len(nums)
    
    min_dp = [[INF] * N for i in range(N)]
    max_dp = [[-INF] * N for i in range(N)]
    
    for i in range(N):
        min_dp[i][i] = max_dp[i][i] = nums[i]
    
    for size in range(1, N): # 부분배열 크기
        for i in range(N - size): # 시작점
            j = i + size # 끝점
            for k in range(i, j):
                if ops[k] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    return max_dp[0][-1]
    