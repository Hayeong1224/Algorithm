#include <iostream>
using namespace std;

int main(void) {
    int N, temp, cnt;
    cin >> N;
    cnt = N;
    for(int i=0; i<N; i++) {
        cin >> temp;
        if(temp == 1 ){
            cnt--;
            continue;
        } else {
            for(int j=2; j<temp; j++){
                if(temp%j == 0) {
                    cnt --;
                    break;
                }
            }
        }
    }
    cout << cnt;
}