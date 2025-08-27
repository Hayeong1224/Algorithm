#include <bits/stdc++.h>
using namespace std;

//board
//vis
//n,m
//dx, dy

int board[501][501];
bool vis[501][501];
int n, m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int num, maxSize;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    //일단 n,m이랑 보드 입력 받기
    cin >> n >> m;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++) {
            cin >> board[i][j];
        }
    }

    //모든 그림의 시작점 넣기
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++) {
            //그림이고 방문 안 한 점만
            if(board[i][j]==0 || vis[i][j]) continue;
            num++; //그림  수 ++
            queue<pair<int, int> > Q; //그림마다 큐 생성
            vis[i][j] = 1;
            Q.push({i,j});
            int size = 0; //그림마다 사이즈 재기
            while(!Q.empty()){
                pair<int,int> cur = Q.front();
                size++; //칸 하나씩 있을 때마다(= pop할 떄마다) 사이즈 ++
                Q.pop();
                for(int dir=0; dir<4; dir++){
                    int nx = cur.first + dx[dir];
                    int ny = cur.second + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if(vis[nx][ny] || board[nx][ny] == 0) continue;
                    vis[nx][ny] = 1;
                    Q.push({nx,ny}); 
                }
            }
            //그림 하나 방문 끝
            maxSize = max(maxSize, size);
        }
    }

    //끝
    cout << num << '\n' << maxSize;
}