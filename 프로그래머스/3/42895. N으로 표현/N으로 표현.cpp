#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int N, int number) {
    vector<set<int> > dp(9);
    
    for (int i = 1; i < 9; i++) { // i번 사용한 수
        string str = "";
        for (int j = 0; j < i; j++) str += to_string(N);
        dp[i].insert(stoi(str));
        for (int j = 0; j < i/2 + 1; j++) {
            for (auto op1 : dp[j]) {
                for (auto op2 : dp[i - j]) {
                    dp[i].insert(op1 + op2);
                    dp[i].insert(op1 - op2);
                    dp[i].insert(op2 - op1);
                    dp[i].insert(op1 * op2);
                    if (op2 != 0) dp[i].insert(op1 / op2);
                    if (op1 != 0) dp[i].insert(op2 / op1);
                }
            }
        }
        
        if (dp[i].find(number) != dp[i].end()) return i;
    }
    
    return -1;
}