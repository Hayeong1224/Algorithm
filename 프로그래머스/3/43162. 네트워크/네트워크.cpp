#include <string>
#include <vector>

using namespace std;

bool visited[200];

void dfs(int cur, int n, const vector<vector<int>>& computers) {
    visited[cur] = true;
    for(int nxt = 0; nxt < n; nxt++) {
        if(computers[cur][nxt] == 1 && !visited[nxt]) {
            dfs(nxt, n, computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int ans = 0;
    
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, n, computers);
            ans ++;
        }
    }
    
    return ans;
}