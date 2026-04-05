#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

bool is_enable_to_change(string& a, string& b) {
    int cnt = 0;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) cnt ++;
    }
    return cnt == 1;
}

int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()) return 0;
    
    vector<bool> visited(words.size(), false);
    queue <pair<string, int> > q;
    q.push({begin, 0});
    
    while(!q.empty()) {
        auto [cur, dist] = q.front();
        q.pop();
        
        if (cur == target) return dist;
        
        for (int i = 0; i < words.size(); i++) {
            if (!visited[i] && is_enable_to_change(cur, words[i])) {
                visited[i] = true;
                q.push({words[i], dist + 1});
            }
        }
    }
    
    return 0;
}