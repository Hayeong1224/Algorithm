#include <iostream>
using namespace std;
int world[500];
int main(){
    int H, W;
    cin >> H >> W;
    for(int i=0; i<W; i++) cin >> world[i];
    int result = 0; 
    for(int i=1;i<W-1;i++) {
        int left = 0, right =  0;
        for(int j=0; j<i; j++) left = max(left, world[j]);
        for(int j=i+1; j<W; j++) right = max(right, world[j]);
        result += max(0, min(left, right) - world[i]);
    }
    cout << result;
}