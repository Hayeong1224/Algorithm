#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    deque <pair<int, int> > q;
    for (int i = 0; i < priorities.size(); i++) {
        q.push_back({i, priorities[i]});
    }
    
    vector<int> answer(priorities.size(), 0);
    int t = 1;
    while (!q.empty()) {
        auto it = max_element(q.begin(), q.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        }); 
        
        int max_val = it->second;
        
        auto [i, p] = q.front();
        q.pop_front();
        if (max_val == p) { // 우선 순위가 가장 큰 프로세스면 실헹
            answer[i] = t;
            t ++;
        } else {
            q.push_back({i, p});
        }
        
    }
    return answer[location];
}