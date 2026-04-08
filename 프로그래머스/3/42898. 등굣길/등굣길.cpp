#include <string>
#include <vector>

using namespace std;


int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<int> > dp(n+1, vector<int>(m+1, 0));
    
    dp[1][1] = 1;
    for (auto p : puddles) {
        dp[p[1]][p[0]] = -1;
    }
    
    for (int i = 1; i < n+1; i++) {
        for (int j = 1; j < m+1; j++) {
            
            if (i==1 && j==1) continue;
            if (dp[i][j] == -1) {
                dp[i][j] = 0;
                continue;
            }
            
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007;
        }
    }
    
    return dp[n][m];
}