#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int ans = n;
    
    for (int i = 0; i < wires.size(); i++) { 
        // 1. 인접 리스트 - i 제외       
        vector<vector<int>> adj(n+1);
        
        for (int j = 0; j < wires.size(); j++) {
            if (i == j) continue;
            int u = wires[j][0];
            int v = wires[j][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        // 2. BFS로 네트워크 노드 세기
        vector<bool> visited(n+1, false);
        queue<int> q;
        q.push(1);
        visited[1] = true;
        int cnt = 0;
        
        while(!q.empty()) {
            int cur = q.front();
            q.pop();
            cnt ++;
            
            for(int next : adj[cur]) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }
        
        int diff = abs(cnt - (n - cnt));
        ans = min(ans, diff);
    }
    
    return ans;
}