#include <string>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int board[101][101];

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    /** 테두리 만들기 **/
    for (auto rect: rectangle) {
        for (int x = rect[0]*2; x <= rect[2]*2; x++) {
            for (int y = rect[1]*2; y <= rect[3]*2; y++) {
                board[x][y] = 1;
            }
        }
    }
    
    for (auto rect: rectangle) {
        for (int x = rect[0]*2+1; x < rect[2]*2; x++) {
            for (int y = rect[1]*2+1; y < rect[3]*2; y++) {
                board[x][y] = 0;
            }
        }
    }
    
    /** 이동 **/
    int dx[] = {0,1,0,-1};
    int dy[] = {1,0,-1,0};
    
    queue<tuple<int, int, int> > q;
    q.push({characterX*2, characterY*2, 0});
    board[characterX*2][characterY*2] = 0;
    
    while(!q.empty()) {
        auto [cx, cy, dist] = q.front();
        q.pop();
        
        if (cx == itemX*2 && cy == itemY*2) return dist/2;
        
        for (int i=0; i<4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            
            if (0<=nx && nx<101 && 0<=ny && ny<101 && board[nx][ny] == 1) {
                board[nx][ny] = 0;
                q.push({nx, ny, dist+1});
            }
        }
    }
    
    return -1;
}