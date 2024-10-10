#include <bits/stdc++.h>
using namespace std;

bool visited[11][11][4];
int dx[] = {0,-1,0,1}; //u,l,d,r
int dy[] = {-1,0,1,0};

int checkDir(char dir){
    if(dir == 'U')  return 0;
    else if(dir == 'L')  return 1;
    else if(dir == 'D')  return 2;
    else  return 3;
}

bool checkWall(int x, int y){ return x<0 || y<0 || x>10 || y>10;}

int solution(string dirs) {
    int answer = 0;
    int x=5, y=5;
    
    for(auto c: dirs) {
        int dir = checkDir(c);
        int tmpX = x+dx[dir];
        int tmpY = y+dy[dir];

        if(checkWall(tmpX,tmpY)) continue;
        
        if(!visited[y][x][dir]){
            visited[y][x][dir] = true;
            visited[tmpY][tmpX][(dir+2)%4] = true;
            answer++;
        }     
        x=tmpX;
        y=tmpY;
    }
    
    return answer;
}