#include<bits/stdc++.h>
using namespace std;

//1차원 BFS 문제
int dist[100002];
int dx[3] = {1, -1, 2};
queue<int> Q;
int n, k;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fill(dist,dist+100002,-1);
    cin >> n >> k;
    dist[n] = 0;
    Q.push(n);

    while(!Q.empty()) {
        auto cur = Q.front();
        Q.pop();
        for(int dir=0;dir<3;dir++) {
            int nx;
            if(dir<2) nx = cur + dx[dir];
            else nx = cur*dx[dir];
            if(nx < 0 || nx > 100000) continue;
            if(dist[nx] != -1) continue;
            dist[nx] = dist[cur] + 1;
            Q.push(nx);
        }
    }
    cout << dist[k];
}