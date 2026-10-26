#include <string>
#include <vector>

using namespace std;

void dfs(int cur, int n, const vector<vector<int> >& computers, vector<bool>& visited) {
    visited[cur] = true;
    for (int nxt = 0; nxt < n; nxt++) {
        if (computers[cur][nxt] == 1 && !visited[nxt]) {
            dfs(nxt, n, computers, visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    vector<bool> visited(n, false);
    
    for (int i=0; i<n; i++) {
        if (!visited[i]) {
            answer += 1;
            dfs(i, n, computers, visited);
        }
    }
    
    return answer;
}