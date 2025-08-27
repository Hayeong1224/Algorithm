#include<bits/stdc++.h>
using namespace std;

int r,c;
char board[1002][1002];
int distJ[1002][1002];
int distF[1002][1002];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

queue<pair<int,int> > QJ;
queue<pair<int,int> > QF;
int minDist;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> r >> c;
    for(int i=0;i<r;i++) {
        for(int j=0;j<c;j++) {
            cin >> board[i][j];
            if(board[i][j] == 'J') {
                distJ[i][j] = 0;
                QJ.push({i,j});
            }
            if(board[i][j] == 'F') {
                distF[i][j] = 0;
                QF.push({i,j});
            }
            if(board[i][j] != '.') continue;
            distJ[i][j] = -1;
            distF[i][j] = -1;
        }
    }

    while(!QF.empty()) {
        auto cur = QF.front();
        QF.pop();
        for(int dir=0;dir<4;dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx<0 || nx>=r || ny<0 || ny>=c) continue;
            if(distF[nx][ny] != -1) continue;
            distF[nx][ny] = distF[cur.first][cur.second]+1;
            QF.push({nx,ny});
        }
    }

    while(!QJ.empty()) {
        auto cur = QJ.front();
        QJ.pop();

        if(cur.first==0 || cur.first==r-1 || cur.second==0 || cur.second==c-1) {
            cout << distJ[cur.first][cur.second]+1;
            return 0;
        }

        for(int dir=0;dir<4;dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx<0 || nx>=r || ny<0 || ny>=c) continue;
            if(distJ[nx][ny] != -1) continue;
            distJ[nx][ny] = distJ[cur.first][cur.second]+1;
            if(distF[nx][ny] != -1 && distJ[nx][ny] >= distF[nx][ny]) {
                distJ[nx][ny] = -2;
                continue;
            }
            QJ.push({nx,ny});
        }
    }

    cout << "IMPOSSIBLE";
}