def solution(arr):
    # 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 함 -> 최대값과 최솟값 계산
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    N = len(nums)
    
    # dp[i][j] : i번째 숫자부터 j번째 숫자까지 연산 결과
    min_dp = [[float('inf')] * N for i in range(N)]
    max_dp = [[-float('inf')] * N for i in range(N)]
    
    for i in range(N):
        min_dp[i][i] = max_dp[i][i] = nums[i]
    
    # 구간의 길이(size)를 1무터 N-1까지 늘려가며 확인
    for size in range(1, N):
        for i in range(N - size): # 시작점
            j = i + size # 끝점
            for k in range(i, j): # 괄호 나누는 지점 선택
                if ops[k] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    return max_dp[0][-1] # 0부터 마지막까지 계산한 최댓값