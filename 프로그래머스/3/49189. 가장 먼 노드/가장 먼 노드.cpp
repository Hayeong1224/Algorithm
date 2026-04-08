#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    // 인접 리스트 만들기
    vector<vector<int> > adj(n+1);
    
    for (auto nodes : edge) {
        auto v1 = nodes[0];
        auto v2 = nodes[1];
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }
    
    // bfs 돌리기 - (node, dist) -> 가장 먼 길이, 가장 먼 노드 개수
    queue<pair<int, int> > q;
    vector<bool> visited(n+1, false);
    
    q.push({1, 0});
    visited[1] = true;
    
    int maxDist = 0;
    int maxNodeCnt = 0;
    
    while (!q.empty()) {
        auto [cn, dist] = q.front();
        q.pop();
        
        // 가장 먼 길이 및 노드 개수 갱신
        if (maxDist < dist) {
            maxDist = dist;
            maxNodeCnt = 1;
        } else if (maxDist == dist) {
            maxNodeCnt ++;
        }
        
        for (auto n : adj[cn]) {
            if (!visited[n]) {
                visited[n] = true;
                q.push({n, dist+1});
            }
        }
    }
    
    return maxNodeCnt;
}