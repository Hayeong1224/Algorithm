#include <vector>
#include <string>
using namespace std;

int solution(vector<string> arr)
{
    vector<int> nums;
    vector<string> ops;
    
    for (int i = 0; i < arr.size(); i++) {
        if (i%2 == 0) nums.push_back(stoi(arr[i]));
        else ops.push_back(arr[i]);        
    }
    
    const int n = nums.size();
    const int INF = int(1e9);
    
    vector<vector<int> > max_dp(n, vector<int>(n, -INF));
    vector<vector<int> > min_dp(n, vector<int>(n, INF)); 
    
    for (int i = 0; i < n; i++) {
        max_dp[i][i] = nums[i];
        min_dp[i][i] = nums[i];
    }
    
    // 구간 늘려가며 업데이트
    for (int size = 1; size < n; size ++) {
        for (int i = 0; i < n - size; i++) {
            int j = i + size;
            for (int k = i; k < j; k ++) {
                if (ops[k] == "+") {
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]);
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]);
                } else {
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]);
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]);
                }
            }
        }
    }
    
    return max_dp[0][n-1];
}