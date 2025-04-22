#include <iostream>
using namespace std;
int world[500];
int main(){
    int H, W;
    cin >> H >> W;
    for(int i=0; i<W; i++) cin >> world[i];
    bool searching = true;
    int max = 0, index = 0, result = 0; 
    for(int i=0;i<W;i++) {
        // 탐색
        if (searching) {
            for(int j=i+1;j<W;j++) {
                if(max < world[j]) {
                    max = world[j];
                    index = j;
                }
                // 더 높은 블록을 찾았을 때 빗물 용량 구하러 가기
                if(world[i] <= max) {
                    max = world[i];
                    searching = false;
                    break;
                }
            }
            // 마지막까지 더 높은 블록을 못 찾았을 때 빗물 용량 구하러 가기
            if(world[i] > max) searching = false;
        } else { // 빗물 용량 구하기
            if(i < index) {
                if(max == 0) break;
                if(max - world[i] > 0) result += max - world[i];
            }
            else {
                max = 0;
                searching = true;
                i--;
            }
        }
    }
    cout << result;
}