#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> dfs(const vector<vector<string>>& tickets, vector<bool>& used, string cur, vector<string>& path) {
    if (find(used.begin(), used.end(), false) == used.end()) return path;
    
    for (int i=0; i<tickets.size(); i++) {
        if (tickets[i][0] == cur && !used[i]) {
            used[i] = true;
            path.push_back(tickets[i][1]);
            
            vector<string> res = dfs(tickets, used, tickets[i][1], path);
            if (!res.empty()) return res;
            
            used[i] = false;
            path.pop_back();
        }
    }
    
    return {};
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end(), [](const vector<string>& a, const vector<string>& b) {return a[1] < b[1];});
    
    int n = tickets.size();
    vector<bool> used(n, false);
    vector<string> path = {"ICN"};
    
    return dfs(tickets, used, "ICN", path);
}