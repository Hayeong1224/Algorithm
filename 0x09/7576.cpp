#include<bits/stdc++.h>
using namespace std;
int board[1002][1002];
int dist[1002][1002];
int n, m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
queue<pair<int,int> > Q;
int ans;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >> n;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++) {
            cin >> board[i][j];
            if(board[i][j] == 1) Q.push({i,j});
            else if(board[i][j] == 0) dist[i][j]= -1;
        }
    }
    while(!Q.empty()){
        pair<int,int> cur = Q.front();
        Q.pop();
        for(int dir=0; dir<4; dir++){
            int nx = cur.first+dx[dir];
            int ny = cur.second+dy[dir];
            if(nx<0 || nx>=n || ny<0 || ny>=m) continue;
            if(dist[nx][ny] >= 0) continue;
            dist[nx][ny] = dist[cur.first][cur.second]+1;
            Q.push({nx,ny});
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++) {
            if(dist[i][j] == -1) { //모두 익지 못한 경우
                cout << -1;
                return 0;
            }
            ans = max(ans, dist[i][j]); //모든 토마토가 익어있는 경우면 매번 max(0,0)이니까 0이 나옴
        }
    }
    cout << ans;
}