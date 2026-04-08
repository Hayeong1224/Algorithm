#include <string>
#include <vector>
#include <queue>
#include <set>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> results) {    
    // 정확하게 순위를 매길 수 있는 기준??? 나머지 모든 사람과의 승패 관계가 확실.
    vector<set<int> > winAdj(n+1); // 이길 수 있는 사람 리스트
    vector<set<int> > loseAdj(n+1); // 지는 사람 리스트
    for (auto match : results) {
        winAdj[match[0]].insert(match[1]);
        loseAdj[match[1]].insert(match[0]);
    }
    
    int ans = 0;
    // 사람 별로 bfs로 타고 가기!!
    // - b한테 이김 -> b의 winAdj한테는 다 이김! -> winAdj[node]에 winAdj[b] 요소들 추가
    // - b힌테 짐 -> b의 loseAdj한테는 다 짐! -> loseAdj[node]에 loseAdj[b] 요소들 추가
    for (int i=1; i < n+1; i++) {
        
        // 이긴 사람 수 세기
        queue <int> q;
        vector <bool> w_visited(n+1, false);
        q.push(i);
        w_visited[i] = true;
        int w_cnt = 0;
        
        while(!q.empty()) {
            auto node = q.front();
            q.pop();
            
            for (auto n_node : winAdj[node]) {
                if(!w_visited[n_node]) {
                    w_visited[n_node] = true;
                    q.push(n_node);
                    w_cnt ++;
                }
            }
        }
        
        // 진 사람 수 세기
        vector <bool> l_visited(n+1, false);
        q.push(i);
        l_visited[i] = true;
        int l_cnt = 0;
        
        while(!q.empty()) {
            auto node = q.front();
            q.pop();
            
            for (auto n_node : loseAdj[node]) {
                if(!l_visited[n_node]) {
                    l_visited[n_node] = true;
                    q.push(n_node);
                    l_cnt ++;
                }
            }
        }
        
        if (w_cnt + l_cnt == n - 1) ans ++;
    }
    
    return ans;    
}