#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    multiset<int> ms; // 오름차순으로 자동 정렬되는 집합
    
    for (auto op :operations) {
        char cmd = op[0];
        int num = stoi(op.substr(2));
        
        if (cmd == 'I') {
            ms.insert(num);
        } else {
            if (ms.empty()) continue;
            
            if (num == -1) {
                ms.erase(ms.begin());
            } else {
                auto it = prev(ms.end());
                ms.erase(it);
            }
        }
    }
    
    if (ms.empty()) return {0, 0};
    
    return {*prev(ms.end()), *ms.begin()};
}