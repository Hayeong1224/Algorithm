#include<vector>
#include<queue>

using namespace std;

struct Pos {
    int x, y;
};

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    
    queue<Pos> q;
    q.push({0,0});
    
    while (!q.empty()) {
        Pos cur = q.front();
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            
            if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1) {
                maps[nx][ny] = maps[cur.x][cur.y] + 1;
                q.push({nx,ny});
            }
        }
    }
    
    return maps[n-1][m-1] > 1 ? maps[n-1][m-1] : -1;
}