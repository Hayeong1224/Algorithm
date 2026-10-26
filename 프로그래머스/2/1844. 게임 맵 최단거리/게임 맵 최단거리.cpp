#include <vector>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    
    // dist 기록 필요! -> maps에 기록
    queue<pair<int, int> > q;
    q.push({0,0});
    
    while(!q.empty()) {
        auto [x,y] = q.front();
        q.pop();
        
        if (x == n-1 && y == m-1) {
            return maps[n-1][m-1];
        }
        
        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny] == 1) {
                maps[nx][ny] = maps[x][y] + 1;
                q.push({nx,ny});
            }
        }
        
    }
    
    return -1;
}