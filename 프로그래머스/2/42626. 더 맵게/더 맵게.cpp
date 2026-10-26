#include <string>
#include <vector>
#include <queue>

// 최소힙 사용

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (const auto& val : scoville) {
        pq.push(val);
    }
    
    // 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    while(pq.top() < K) {
        if(pq.size() < 2) return -1;
        
        answer += 1;
        int f_val = pq.top();
        pq.pop();
        int s_val = pq.top();
        pq.pop();
        
        int new_val = f_val + 2 * s_val;
        pq.push(new_val);
    }
    
    return answer;
}