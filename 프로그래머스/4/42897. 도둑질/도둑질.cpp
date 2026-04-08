#include <string>
#include <vector>

using namespace std;

int solution(vector<int> money) {
    const int n = money.size();
    
    // 첫 집 털기 -> 마지막 집 안 털기
    vector<int> dp1(n, 0);
    dp1[0] = money[0];
    dp1[1] = dp1[0];
    for (int i=2; i<n-1; i++) {
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1]);
    }
        
    // 첫 집 안 털기
    vector<int> dp2(n, 0);
    dp2[0] = 0;
    dp2[1] = money[1];
    for (int i=2; i<n; i++) {
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1]);
    }
    
    return max(dp1[n-2], dp2[n-1]);
}