#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int ans = 0;
    int n = dungeons.size();
    
    vector<int> p;
    for(int i = 0; i < n; i++) p.push_back(i);
    
    do {
        int cur_k = k;
        int cnt = 0;
        
        for(int i = 0; i < n; i++) {
            int idx = p[i];
            if(cur_k >= dungeons[idx][0] && cur_k - dungeons[idx][1] >= 0) {
                cur_k -= dungeons[idx][1];
                cnt ++;
            } else break;
        }
        ans = max(ans, cnt);
            
        } while(next_permutation(p.begin(), p.end()));
    
    return ans;
}