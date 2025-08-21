#include<bits/stdc++.h>
using namespace std;

int M, N;
int Map[8][8];
vector<pair<int, int>> CCTV;

int dy[4] = {-1,0,1,0}; //상, 좌, 하, 우
int dx[4] = {0,-1,0,1};

int result = 10000;

/*
1 -> 한 방향(상) - 0
2 -> 반대 두 방향(상하) - 0,2
3 -> 수직 두 방향(상좌) - 0,1
4 -> 세 방향(상좌하) - 0,1,2
5 -> 모든 방향(상좌하우) - 0,1,2,3
*/

void check(int y, int x, int dir){
    cout << "체크" << '\n';
    dir %= 4;
    while(1) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];
        y = ny;
        x = nx;
        if(ny<0 || nx<0 || ny>=N || nx>=M) return;
        if(Map[ny][nx] == 6) return;
        if(Map[ny][nx] != 0) continue;
        Map[ny][nx] = -1;
    }
}

void dfs(int idx){
    cout << "dfs 시작" << '\n';
    //끝내는 조건 - 모든 cctv 확인 다 했을 때
    if(idx == CCTV.size()) {
        int cnt = 0;
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++) 
                if(Map[i][j]==0) cnt++;

        result = min(result, cnt);
        return;
    }

    int y = CCTV[idx].first;
    int x = CCTV[idx].second;
    int backup[8][8];

    //4방향 회전
    for(int dir=0; dir <4; dir++) {
        for(int i=0; i<N;i++)
            for(int j=0;j<M;j++)
                backup[i][j] == Map[i][j];

        if(Map[y][x] == 1) check(y, x, dir);
        else if (Map[y][x] == 2) {
            check(y, x, dir);
            check(y, x, dir+2);
        }else if (Map[y][x] == 3) {
            check(y, x, dir);
            check(y, x, dir + 1);
        }else if (Map[y][x] == 4) {
            check(y, x, dir);
            check(y, x, dir + 1);
            check(y, x, dir + 2);
        }else if (Map[y][x] == 5){
            check(y, x, dir);
            check(y, x, dir + 1);
            check(y, x, dir + 2);
            check(y, x, dir + 3);
        }
        cout << "다음 dfs" << '\n';
        dfs(idx+1);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                Map[i][j] = backup[i][j];
    }
}

int main(void)
{
    cin >> N >> M;
    cout << "입력 시작" << '\n';
    for (int i = 0; i < N; i++){ // 세로 길이만큼
        for (int j = 0; j < M; j++){ // 가로 길이만큼
            cin >> Map[i][j];
            if (0 < Map[i][j] && Map[i][j] < 6)
                CCTV.push_back(make_pair(i, j));
        }
    }
    cout << "입력 완료" << '\n';
    dfs(0);
    cout << result;
}