#include<bits/stdc++.h>
using namespace std;

struct room{
    int num;
    int grade;
    int gender = -1;
};
room rooms[1001];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    cin >> N >> K;

    for(int i=0;i<N;i++){
        int S, Y;
        cin >> S >> Y;
        for(int j=0;j<1001;j++){
            if(rooms[j].num < K){
                if(rooms[j].gender<0){
                    rooms[j].num++;
                    rooms[j].gender= S;
                    rooms[j].grade = Y;
                    break;
                }
                else if(rooms[j].gender == S && rooms[j].grade == Y){
                    rooms[j].num++;
                    break;
                }
            }
        }
    }

    int cnt = 0;
    while(rooms[cnt].num>0) cnt ++;
    cout << cnt;
}