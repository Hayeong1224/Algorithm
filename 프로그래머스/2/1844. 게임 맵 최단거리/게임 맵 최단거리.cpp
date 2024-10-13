#include<bits/stdc++.h>
using namespace std;

int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};
bool visited[100][100];
int dist[100][100];  // 각 좌표까지의 최단 거리를 저장
int N, M;
int board[100][100];

bool canGo(int y, int x){
    return y < N && 0 <= y && x < M && 0 <= x && (board[y][x] == 1);
}

int bfs(int y, int x){
    queue<pair<int,int>> q;
    q.push(make_pair(y, x));
    visited[y][x] = true;
    dist[y][x] = 1;  // 시작점의 거리는 1로 초기화

    while(!q.empty()){
        pair<int,int> cur = q.front();
        q.pop();
        for(int k=0; k<4; k++){
            int ny = cur.first + dy[k], nx = cur.second + dx[k];
            if(canGo(ny, nx) && !visited[ny][nx]) {
                q.push(make_pair(ny,nx));
                visited[ny][nx] = true;
                dist[ny][nx] = dist[cur.first][cur.second] + 1;  // 이전 칸 거리 + 1
            }
        }
    }
    
    // (N-1, M-1) 위치에 도착할 수 있으면 해당 위치까지의 최단 거리 반환
    if(visited[N-1][M-1]) return dist[N-1][M-1];
    else return -1;
}

int solution(vector<vector<int>> maps)
{
    N = maps.size();
    M = maps[0].size();
    
    // 초기화
    memset(visited, false, sizeof(visited));
    memset(dist, 0, sizeof(dist));
    
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++) board[i][j] = maps[i][j];
    
    return bfs(0, 0);
}
