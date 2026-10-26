#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>

using namespace std;

unordered_map<char, pair<int, int> > dir = {
    {'E', {0, 1}},
    {'W', {0, -1}},
    {'N', {-1, 0}},
    {'S', {1, 0}}
};

vector<int> solution(vector<string> park, vector<string> routes) {
    
    vector<int> cpos(2, 0);
    
    // S 찾기!
    for (int x=0; x<park.size(); x++) {
        for (int y=0; y<park[0].size(); y++) {
            if (park[x][y] == 'S') {
                cpos[0] = x;
                cpos[1] = y;
            }
        }
    }
    
    for (const auto& route: routes) {
        stringstream ss(route);
        char op;
        int n;
        ss >> op >> n;
        
        auto [dr, dc] = dir[op]; 
        
        // 현재 위치를 임시 좌표에 복사
        int nx = cpos[0];
        int ny = cpos[1];
        bool possible = true;
        
        for(int i=0; i<n; i++) {
            nx += dr;
            ny += dc;
            
            if (nx < 0 || nx >= park.size() || ny < 0 || ny >= park[0].size() || park[nx][ny] == 'X') {
                possible = false;
                break;
            }
        }
        
        if (possible) {
            cpos[0] = nx;
            cpos[1] = ny;
        }
        
    }

    return cpos;
}