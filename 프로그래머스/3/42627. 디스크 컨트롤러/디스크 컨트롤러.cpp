#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int total_return_time = 0;
    int n = jobs.size();
    int now = 0;
    int start = -1;
    int i = 0; // 끝낸 작업 개수
    
    sort(jobs.begin(), jobs.end());
    
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
    while (i < n) {
        //pq에 요청 작업 넣기
        for (auto j : jobs) {
            int term = j[1];
            int ask = j[0];
            if (start < ask && ask <= now) pq.push({term, ask});
            else if (ask > now) break;
        }
        
        if (!pq.empty()) {
            auto [term, ask] = pq.top(); pq.pop();
            start = now;
            now += term;
            total_return_time += (now - ask);
            i ++;
            
        } else {
            now = jobs[i][0];
        }
        
    }
    
    return int(total_return_time / n);
}